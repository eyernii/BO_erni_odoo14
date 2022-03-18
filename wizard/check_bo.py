from odoo import fields, models


class check_bo_wizard(models.TransientModel):
    _name = 'check.bo.wizard'
    _description = 'New Description'

    message = fields.Text(string='Message', stored=False)

