from odoo import api, models, fields
from odoo.exceptions import UserError

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
        if check == True and self.plan_sale_order_id.state == 'send':
            self.check_approver = True
        else:
            self.check_approver = False

    def btn_approve(self):
        approver = int(self.approver)
        approver_current = int(self.env.user.partner_id)
        if approver_current == approver:
            self.approval_status = 'approve'
            approver_id = self.plan_sale_order_id.approver_id
            list_status = approver_id.mapped('approval_status')
            if all(x == 'approve' for x in list_status):
                self.plan_sale_order_id.state = 'approve'
                self.plan_sale_order_id.message_post(body=f'{self.env.user.name}-> {self.plan_sale_order_id.name} plan has been approve.')
        else:
            raise UserError("This is not allowed approve")
    def btn_refuse(self):
        approver = int(self.approver)
        approver_current = int(self.env.user.partner_id)
        if approver_current == approver:
            self.approval_status = 'refuse'
            approver_id = self.plan_sale_order_id.approver_id
            list_status = approver_id.mapped('approval_status')
            if all(x == 'refuse' for x in list_status):
                self.plan_sale_order_id.state = 'refuse'
                self.plan_sale_order_id.message_post(body=f'{self.env.user.name}-> {self.plan_sale_order_id.name} plan has been refused.')
        else:
            raise UserError("This is not allowed approve")
