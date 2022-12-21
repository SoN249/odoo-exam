from odoo import api, fields, models


class ESalesOrder(models.Model):
    _inherit = "sale.order"

    plan_sale = fields.Many2one('plan.sale.order', string='Plan sale order')

    def create_plan_sale(self):
        if self.plan_sale and self.plan_sale.check_confirm == True:
            return super(ESalesOrder, self).create_plan_sale()
        else:
            raise models.ValidationError('The business plan has not been added or approved yet')