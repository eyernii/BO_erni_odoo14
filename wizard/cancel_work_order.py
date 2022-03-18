from odoo import fields, models


class CancellationWorkOrder(models.TransientModel):
    _name = 'cancellation.workorder'
    _description = 'Message cancellation work order'

    notes = fields.Text(string='Reason')

    def action_cancel(self):
            self.env['sale.work.order'].browse(self.env.context['active_id']).update({'notes':self.notes, 'state':'cancelled'})
