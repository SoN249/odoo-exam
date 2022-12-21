from odoo import api,models, fields
from datetime import date
class IndicatorEvaluationCronjob(models.Model):
    _inherit = 'indicator.evaluation'

    revenue_difference = fields.Float('Revenue Difference', compute='_compute_revenue_difference', store=True)

    def _compute_revenue_difference(self):
        current_month = date.today().month
        for rec in self:
            if rec.real_revenue:
                month_sales_result = self.env['crm.team'].search([('id', 'in', rec.sale_team.mapped('id'))])
                month_sales = month_sales_result.mapped(lambda res: (res.month_1, res.month_2,
                                                                     res.month_3, res.month_4, res.month_5,
                                                                     res.month_6, res.month_7, res.month_8,
                                                                     res.month_9, res.month_10,
                                                                     res.month_11, res.month_12))
                print(month_sales)
                rec.revenue_difference = rec.real_revenue - month_sales[0][current_month - 1]