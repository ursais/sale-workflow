# Copyright 2024
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class SaleOrder(models.Model):
    """Extend sale.order to add requires_service_report field."""
    _inherit = 'sale.order'

    requires_service_report = fields.Boolean(
        string='Requires Service Report',
        compute='_compute_requires_service_report',
        store=True,
        readonly=True,
        help='Indicates whether a service report is required for this sales order. '
             'This is based on the billing/invoicing partner setting.',
    )

    @api.depends('partner_invoice_id', 'partner_invoice_id.requires_service_report',
                 'partner_id', 'partner_id.requires_service_report')
    def _compute_requires_service_report(self):
        """
        Compute requires_service_report based on the billing/invoicing partner.
        If partner_invoice_id is set, use its value; otherwise use partner_id.
        """
        for order in self:
            partner = order.partner_invoice_id or order.partner_id
            order.requires_service_report = partner.requires_service_report if partner else False
