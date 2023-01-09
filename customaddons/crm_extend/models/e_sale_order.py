from odoo import api, fields, models
class ESalesOrder(models.Model):
    _inherit = "sale.order"

    plan_sale = fields.Many2one('plan.sale.order', string='Plan sale order')

    def create_plan_sale(self):
        # Open form plan sale order
        return{
            'res_model': 'plan.sale.order',
            'type': 'ir.actions.act_window',
            'view_mode': 'form'
        }
    def action_confirm(self):
        # Check if plan is approve then confirm
      if self.plan_sale and self.plan_sale.state == 'approve':
        return super(ESalesOrder, self).action_confirm()
      else:
        raise models.ValidationError('The business plan has not been added or approved yet')