from odoo import fields, models, api, _

class StockPicking(models.Model):
    _inherit = "stock.picking"


    blanket_id = fields.Many2one(
        "sale.blanket.order",
    )
