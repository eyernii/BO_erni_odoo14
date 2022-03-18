from odoo import _, api, fields, models


class ServiceTeam(models.Model):
    _name = 'sale.serviceteam'
    _description = 'New Description'

    name = fields.Char(string='Team Name', required=True)
    team_leader_id = fields.Many2one(comodel_name='res.users', string='Team Leader') 
    team_member_ids = fields.Many2many(comodel_name='res.users', string='Team Members')





    