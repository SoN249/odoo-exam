from odoo import api, models, fields


class AproverList(models.Model):
    _name = "approver.list"
    _description = "Approver List"

    approver = fields.Many2one('res.partner', string='Approver')
    approval_status = fields.Selection([
        ('not approved yet', 'Not Approved Yet'),
        ('approve', 'Approve'),
        ('refuse', 'Refuse'),
    ], string='Approval Status', default='not approved yet')
    plan_sale_order_id = fields.Many2one('plan.sale.order', string='Plan Sale Order')
    check_approver = fields.Boolean(compute='_compute_check_approver')

    def _compute_check_approver(self):
        approver_current = int(self.env.user.partner_id)
        approver_list = self.plan_sale_order_id.approver_id.approver
        check = approver_current in approver_list.ids
        if check == True:
            self.check_approver = True
        else:
            self.check_approver = False

    def btn_approve(self):
        self.approval_status = 'approve'
        approver_id = self.plan_sale_order_id.approver_id
        list_status = approver_id.mapped('approval_status')
        if all(x == 'approve' for x in list_status):
            self.plan_sale_order_id.state = 'approve'
            self.message_post(body=f'{self.create_uid.name} -> The new plan has been approved.')

    def btn_refuse(self):
        self.approval_status = 'refuse'
        approver_id = self.plan_sale_order_id.approver_id
        list_status = approver_id.mapped('approval_status')
        if all(x == 'refuse' for x in list_status):
            self.plan_sale_order_id.state = 'refuse'
            self.message_post(body=f'{self.create_uid.name}-> The new plan has been refused.')
