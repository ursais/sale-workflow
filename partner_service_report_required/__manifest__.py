# Copyright 2024
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Partner Service Report Required',
    'version': '16.0.1.0.0',
    'category': 'Sales',
    'license': 'AGPL-3',
    'summary': 'Add Requires Service Report field to partners, sales orders, and invoices',
    'description': """
        This module adds a boolean field 'Requires Service Report' to:
        - Partners (res.partner): Can be set manually
        - Sales Orders (sale.order): Computed from the billing/invoicing partner
        - Invoices (account.move): Computed from the partner
        
        The field is visible on the respective forms and helps track which
        customers require service reports for their invoices and sales orders.
    """,
    'author': 'Open Source Integrators',
    'website': 'https://www.opensourceintegrators.com',
    'depends': [
        'sale',
        'account',
    ],
    'data': [
        'views/res_partner.xml',
        'views/sale_order.xml',
        'views/account_move.xml',
    ],
    'installable': True,
    'application': False,
}
