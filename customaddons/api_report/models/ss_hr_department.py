from odoo import models, fields, api
class SSHrDepartment(models.Model):
    _inherit = 'hr.department'

    revenue_difference = fields.Float('Revenue Difference', compute='_compute_revenue_difference', store=True)

    def _compute_revenue_difference(self):
        for rec in self:
            if rec.real_revenue:
                # Calculate revenue difference
                rec.revenue_difference = rec.real_revenue - rec.limit