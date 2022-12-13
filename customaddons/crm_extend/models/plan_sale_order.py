from odoo import api, fields, models
from odoo.exceptions import ValidationError, UserError

class PlanSaleOrder(models.Model):
    _name = 'plan.sale.order'
    _inherit = ['mail.thread']
    _description = "Plan sale order"

    approver = fields.Many2one('res.partner', string='Approver')
    name = fields.Text("Name Plan", required='True')
    quotation = fields.Many2one('sale.order', string="Quotation", readonly="True")
    infor_plan = fields.Text("Infor plan sale", required="True")
    state = fields.Selection(
        [('new','New'),
         ('send', 'Send'),
         ('approve','Approve'),
         ('refuse','Refuse'),
         ], string="State")

    confirm = fields.Selection([('yes', 'Yes'), ('no', 'No'), ('new', 'New')], tracking=True)
    check_send = fields.Selection([
        ('yes', 'Yes'),
        ('no', 'No')
    ], string='Check Send', compute='_compute_check_send')
    approver_id = fields.One2many('approver.list','plan_sale_order_id',string="Approver")

    def btn_new(self):
        self.state = 'new'
        self.approver_id.approval_status = 'not approved yet'

    def btn_send(self):
        if self.state == 'new':
            if self.approver_id.approver:
                self.state = 'send'
                self.approver_id.approval_status = 'not approved yet'
                self.message_post(body=f'{self.create_uid.name} -> The new plan has been sent.')
            else:
                raise UserError('Please write your approvers')
        else:
            raise UserError('Cannot confirm this approve')

    def btn_approve_confirm(self):
        if self.confirm == 'yes':
            if self.approver_id.approver:
                self.state = 'approve'
                self.message_post(body=f'{self.create_uid.name} -> The new plan has been approved.')
            else:
                raise UserError('Please write your approvers.')
        else:
            raise UserError('All approvers have not yet agreed to approve.')

    def btn_refuse_confirm(self):
        if self.check_confirm == 'no':
            self.state = 'refuse'
            self.message_post(body=f'{self.create_uid.name}-> The new plan has been refused.')
        else:
            raise UserError('All approvers who have not yet declined approval.')

    @api.depends('create_uid')
    def _compute_check_send(self):
        current_user_ui = self.env.uid
        for rec in self:
            rec.check_send = 'no'
            if rec.create_uid:
                if rec.create_uid == current_user_ui:
                    rec.check_send = 'yes'