from odoo import api, fields, models
from dateutil.relativedelta import relativedelta
from datetime import *

class WorkOrder(models.Model):
    _name = 'sale.work.order'
    _description = 'Work Order'

    name = fields.Char(string='WO number', readonly=True, default='New', required=True, copy=False)
    sale_order_id = fields.Many2one(comodel_name='sale.order', string='Booking Order Ref')

    sale_order_id = fields.Many2one(comodel_name='sale.order', string='Booking Order Reference')
    
    team_id = fields.Many2one(comodel_name='sale.serviceteam', string='Service Team')
    team_leader_id = fields.Many2one(comodel_name='res.users', string='Service Team Leader')
    team_member_ids = fields.Many2many(comodel_name='res.users', string='Service Team member')
    
    @api.onchange('team_id')
    def onchange_team_id(self):
        for record in self:
            record.team_leader_id = record.team_id.team_leader_id
            record.team_member_ids = record.team_id.team_member_ids

    planned_start = fields.Datetime(string='Planned Start', required=True)

    planned_end = fields.Datetime(string='Planned End', required=True)

    date_start = fields.Datetime(string='Date Start', readonly=True)
    date_end = fields.Datetime(string='Date End', readonly=True)
    state = fields.Selection(string='Status', selection=[('pending', 'Pending'), ('in_progress', 'In Progress'), ('done', 'Done'), ('cancel', 'Cancel')], readonly=True, default='pending', required=True)
    notes = fields.Text(string='Notes')  

    
    
    def action_start(self):
       for record in self:
           record.state="in_progress" 
           record.date_start=datetime.now()

    def action_end(self):
        for record in self:
            record.state="done"
            record.date_end=datetime.now() 

    def action_reset(self):
        for record in self:
            record.state="pending"
            record.date_start=None     
    
    def action_cancel(self):
        for record in self:
            record.state="cancel"


    def popup_cancellation(self):
            return {
            'name': ('Add Reason'),
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'cancellation.work.order',
            'view_id': False,
            'type': 'ir.actions.act_window',
            'target': 'new'
        }

    @api.model
    def create(self, vals):
        # if vals.get('name', 'New') == 'New':
        vals['name'] = self.env['ir.sequence'].next_by_code('sale.work.order') or 'New'
        return super(WorkOrder, self).create(vals)
    
