from odoo import api, models, fields, _
from odoo.exceptions import UserError, ValidationError


class CrmExtend(models.Model):
    _inherit = "crm.lead"
    _description = "Manager CRM"

    revenue = fields.Float("Doanh thu tối thiểu (trước VAT)")
    real_revenue = fields.Float(string='Doan thu thực tế', compute='_compute_real_revenue', store=False)
    check_edit = fields.Integer(string='Count', compute='_check_edit')
    create_month = fields.Integer('Create Month', compute='_compute_create_month', store=True)
    sale_team = fields.Many2many('crm.team', string="Sale team")

    check_priority = fields.Boolean('Check Priority', default=False, compute='_compute_check_priority', store=True)

    def _check_edit(self):
        for rec in self:
            if rec.id:
                rec.check_edit = self.env['sale.order'].search_count([('opportunity_id', '=', rec.id)])

    @api.constrains('revenue')
    def _check_min_revenue(self):
        for r in self:
            if r.revenue <= 0:
                raise ValidationError("Min revenue must > 0")

    def _compute_real_revenue(self):
        for rec in self:
            if rec.id:
                amount_total = self.env['sale.order'].search([('opportunity_id', '=', rec.id)])
                amount_total_opportunity = amount_total.mapped('amount_total')
                rec.real_revenue = sum(amount_total_opportunity)

    @api.depends('create_date')
    def _compute_create_month(self):
        for rec in self:
            if rec.create_date:
                create_date = str(rec.create_date)
                create_month = create_date.split("-")
                rec.create_month = create_month[1]

    @api.depends('priority')
    def _compute_check_priority(self):
        for rec in self:
            rec.check_priority = False
            if rec.priority == '3':
                rec.check_priority = True

    # Override the Lost button again for the groups leader
    def btn_leader_set_lost(self):
        return super(CrmExtend, self).action_set_lost()