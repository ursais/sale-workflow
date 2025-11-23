# Copyright 2024
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class AccountMove(models.Model):
    """Extend account.move to add requires_service_report field."""
    _inherit = 'account.move'

    requires_service_report = fields.Boolean(
        string='Requires Service Report',
        compute='_compute_requires_service_report',
        store=True,
        readonly=True,
        help='Indicates whether a service report is required for this invoice. '
             'This is based on the partner setting.',
    )

    @api.depends('partner_id', 'partner_id.requires_service_report')
    def _compute_requires_service_report(self):
        """
        Compute requires_service_report based on the partner.
        """
        for move in self:
            move.requires_service_report = move.partner_id.requires_service_report if move.partner_id else False
