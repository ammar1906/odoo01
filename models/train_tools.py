from odoo import fields , models, api


class TrainTools(models.Model):
    _name = "train.tools"


    toolname= fields.Char('tool name')

    user_id = fields.Many2one("train.user", "user")

