from odoo import fields, models


class EDepartment(models.Model):
    _inherit = 'hr.department'
    _description = 'Manage department'
    limit = fields.Float('Spending limit', digits=(14,4))
