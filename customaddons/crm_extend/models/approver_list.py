from odoo import api, models, fields


class AproverList(models.Model):
    _name = "approver.list"
    _description = "Approver List"

    approver = fields.Many2one('res.partner', string='Approver')
    approval_status = fields.Selection([
        ('not approved yet', 'Not Approved Yet'),
        ('approve', 'Approve'),
        ('refuse', 'Refuse'),
    ], string='Approval Status')
    plan_sale_order_id = fields.Many2one('plan.sale.order', string='Plan Sale Order')

    def btn_approve(self):
        self.approval_status = 'approve'
        states = self.plan_sale_order_id.approver_id.mapped('approval_status')
        if [state == 'approve' for state in states]:
            self.plan_sale_order_id.check_confirm = True

    def btn_refuse(self):
        self.approval_status = 'refuse'
        states = self.plan_sale_order_id.approver_id.mapped('approval_status')
        if [state == 'refuse' for state in states]:
            self.plan_sale_order_id.check_confirm = False
