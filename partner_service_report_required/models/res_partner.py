# Copyright 2024
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields


class ResPartner(models.Model):
    """Extend res.partner to add requires_service_report field."""
    _inherit = 'res.partner'

    requires_service_report = fields.Boolean(
        string='Requires Service Report',
        default=False,
        help='Indicates whether this partner requires a service report '
             'for invoices and sales orders.',
    )
