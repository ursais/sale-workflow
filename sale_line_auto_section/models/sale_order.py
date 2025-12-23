# Copyright 2025 Open Source Integrators
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import _, fields, models


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    auto_section_category_id = fields.Many2one(
        comodel_name="product.category",
        string="Auto Section Category",
        help="Product category that generated this automatic section. "
        "Used to identify and update auto-generated sections.",
        copy=False,
    )


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def action_organize_lines_by_category(self):
        """Reorganize sale order lines into sections based on product categories.

        This method:
        - Groups product lines by their category
        - Removes only auto-generated sections (preserves manual sections/notes)
        - Creates new section headers for each category
        - Preserves the relative order of manual sections and notes
        """
        self.ensure_one()

        product_lines = self.order_line.filtered(
            lambda line: not line.display_type and line.product_id
        )
        if not product_lines:
            return

        category_groups = {}
        for line in product_lines:
            category = line.product_id.categ_id
            if category not in category_groups:
                category_groups[category] = []
            category_groups[category].append(line)

        sorted_categories = sorted(
            category_groups.keys(),
            key=lambda c: (c.section_sequence, c.name),
        )

        auto_sections = self.order_line.filtered(
            lambda line: line.display_type == "line_section"
            and line.auto_section_category_id
        )
        auto_sections.unlink()

        sequence = 1
        for category in sorted_categories:
            section_title = category.section_title or category.name
            self.env["sale.order.line"].create(
                {
                    "order_id": self.id,
                    "display_type": "line_section",
                    "name": section_title,
                    "sequence": sequence,
                    "auto_section_category_id": category.id,
                }
            )
            sequence += 1

            for line in category_groups[category]:
                line.sequence = sequence
                sequence += 1

        manual_display_lines = self.order_line.filtered(
            lambda line: line.display_type and not line.auto_section_category_id
        )
        for line in manual_display_lines:
            line.sequence = sequence
            sequence += 1

        return {
            "type": "ir.actions.client",
            "tag": "display_notification",
            "params": {
                "title": _("Success"),
                "message": _("Sale order lines have been organized by category."),
                "type": "success",
                "sticky": False,
            },
        }
