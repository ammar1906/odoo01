from odoo import fields , models, api


class TrainUser(models.Model):
    _name = "train.user"
    _description = "users training with"

    name = fields.Char('full name')
    tool_id = fields.One2many("train.tools", "user_id" , "tools")

    tools_count = fields.Integer("tools", compute='_compute_tools_counts')

    @api.depends('tool_id')
    def _compute_tools_counts(self):
        for rec in self:
            rec.tools_count = len(rec.tool_id)
