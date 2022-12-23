from odoo import api, models, fields, _
from odoo.exceptions import UserError, ValidationError

class CrmExtend(models.Model):
    _inherit = "crm.lead"
    _description = "Manager CRM"

    revenue = fields.Float("Doanh thu tối thiểu (trước VAT)")
    real_revenue = fields.Float(string='Doan thu thực tế', compute='_compute_real_revenue', store=False)
    create_month = fields.Integer('Create Month', compute='_compute_create_month', store=True)
    sale_team = fields.Many2many('crm.team', string="Sale team")
    quotation_count = fields.Integer(compute='_compute_sale_data', string="Number of Quotations")
    check_priority = fields.Boolean('Check Priority', default=False, compute='_compute_check_priority', store=True)

    def _get_user_id(self):
        current_user_id = self.env.uid
        group_staff_id = int(self.env['crm.team.member'].search([('user_id', '=', current_user_id)]).crm_team_id)
        sales_staff_in_group = self.env['crm.team.member'].search([('crm_team_id', '=', group_staff_id)]).user_id.ids
        desired_group_name = self.env['res.groups'].search([('name', '=', 'Leader')])
        is_desired_group = self.env.user.id in desired_group_name.users.ids
        if is_desired_group == True:
            return ""
        else:
            return [('id', 'in', sales_staff_in_group)]

    user_id = fields.Many2one(
        'res.users', string='Salesperson', default=lambda self: self.env.user,
        domain="['&', ('share', '=', False), ('company_ids', 'in', user_company_ids)]" and _get_user_id,
        check_company=True, index=True, tracking=True)
    @api.constrains('revenue')
    def _check_min_revenue(self):
        for r in self:
            if r.revenue <= 0:
                raise ValidationError("Min revenue must more than zero")

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
                rec.create_month = rec.create_date.month
    @api.depends('priority')
    def _compute_check_priority(self):
        for rec in self:
            rec.check_priority = False
            if rec.priority == '3':
                rec.check_priority = True

    # Override the Lost button again for the groups leader
    def btn_leader_set_lost(self):
        return super(CrmExtend, self).action_set_lost()