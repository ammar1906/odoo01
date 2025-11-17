from odoo import fields , models



class SalesOrder(models.Model):
    _inherit = 'sale.order'



    reviews = fields.Char("your reviews")