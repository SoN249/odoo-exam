from odoo import api, models, fields,_
from odoo.exceptions import UserError, ValidationError

class EPurchaseOrder(models.Model):
    _inherit = 'purchase.order'
    department = fields.Many2one('hr.department',string="Department", required="True")
    def button_confirm(self):
            # get role of users
            desired_group_name = self.env['res.groups'].search([('name', '=', 'Accountancy')])
            is_desired_group = self.env.user.id in desired_group_name.users.ids

            current_user_id = self.env.uid
            employee_line = self.env['employee.order.limit'].search([('employee', '=', current_user_id)], limit=1)
            employee = employee_line.mapped('order_limit')

            for rec in self:
                if rec.amount_total:
                    if rec.amount_total < employee[0]:
                        return super(EPurchaseOrder, self).button_confirm()
                    else:
                        if(is_desired_group == False):
                            raise ValidationError('The total request exceeds the limit. Please send it to the accountant.')
                        else:
                            return super(EPurchaseOrder, self).button_confirm()