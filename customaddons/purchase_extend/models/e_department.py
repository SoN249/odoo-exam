from odoo import fields, models, api
from odoo.exceptions import UserError, ValidationError


class EDepartment(models.Model):
    _inherit = 'hr.department'
    _description = 'Manage department'
    limit = fields.Float('Spending limit', digits=(14,4))
    real_revenue = fields.Float(string='Real Revenue', compute='_compute_real_revenue', store=False)
    create_month = fields.Integer('Create Month', compute='_compute_create_month', store=True)

    @api.constrains('spending_limit')
    def _check_spending_limit(self):
        if self.limit:
            if self.limit < 0:
                raise ValidationError("The expected price must be strictly positive")

    # Calculate real_revenue = amount_total corresponding to the department
    def _compute_real_revenue(self):
        for rec in self:
            if rec.name:
                amount_total = self.env['purchase.order'].search([('department', '=', rec.id)])
                amount_total_department = amount_total.mapped('amount_total')
                rec.real_revenue = sum(amount_total_department)

    @api.depends('create_date')
    def _compute_create_month(self):
        for rec in self:
            if rec.create_date:
                create_date = str(rec.create_date)
                create_month = create_date.split("-")
                rec.create_month = create_month[1]