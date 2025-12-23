# Copyright 2025 Open Source Integrators
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import fields, models


class ProductCategory(models.Model):
    _inherit = "product.category"

    section_sequence = fields.Integer(
        default=10,
        help="Sequence order when creating sale order sections by category. "
        "Lower values appear first.",
    )
    section_title = fields.Char(
        help="Title to use when creating sale order sections for this category. "
        "If empty, the category name will be used.",
    )
