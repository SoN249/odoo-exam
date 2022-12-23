from odoo import models, fields, api


class IndicatorEvaluation(models.Model):
    _name = 'indicator.evaluation'

    sale_team = fields.Many2one('crm.team', string='Sale Team')
    real_revenue = fields.Float(string='Real Revenue', compute='_compute_real_revenue', store=False)
    month = fields.Integer('Month', store=True)
    month_revenue = fields.Float('Month Revenue', compute='_compute_month_revenue', store=True)
    create_month = fields.Integer('Create Month', compute='_compute_create_month', store=True)

    # Calculate real_revenue = amount_untaxed corresponding to the opportunity
    def _compute_real_revenue(self):

        for rec in self:
            if rec.sale_team:
                amount_untaxed_opportunity = self.env['sale.order'].search(
                    [('team_id', '=', rec.sale_team.mapped('id'))])
                amount_untaxed = amount_untaxed_opportunity.mapped('amount_untaxed')
                rec.real_revenue = sum(amount_untaxed)

    # Get value month revenue to month of report
    @api.depends('month')
    def _compute_month_revenue(self):
        for rec in self:
            if rec.month:
                month_sales_result = self.env['crm.team'].search([('id', '=', rec.sale_team.mapped('id'))])
                month_sales = month_sales_result.mapped(lambda res: (res.January, res.February, res.March, res.April,
                                                                     res.May, res.June, res.July, res.August, res.September,
                                                                     res.October, res.November, res.December))

                rec.month_revenue = month_sales[0][rec.month - 1]

    @api.depends('create_date')
    def _compute_create_month(self):
        for rec in self:
            if rec.create_date:
                rec.create_month = rec.create_date.month