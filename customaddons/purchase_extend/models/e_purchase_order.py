from odoo import api, models, fields,_


class EPurchaseOrder(models.Model):
    _inherit = 'purchase.order'
    department = fields.Many2one('hr.department',string="Department", required="True")



