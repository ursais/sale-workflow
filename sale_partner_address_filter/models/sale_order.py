# Copyright 2025 Open Source Integrators
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    commercial_partner_id = fields.Many2one(
        related="partner_id.commercial_partner_id",
        readonly=True,
    )

    only_customer_addresses = fields.Boolean(
        string="Select Only Customer Contacts",
        default=True,
        help="When checked, delivery and invoice addresses are filtered "
        "to only show addresses belonging to the customer's commercial company.",
    )
