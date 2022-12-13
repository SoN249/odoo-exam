from odoo import api, models, fields


class EPurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'
    vendors = fields.Char('Vendor Suggest', compute='_compute_vendor', store=True)
    product_id = fields.Many2one('product.product', string='Product', domain=[('purchase_ok', '=', True)],
                                 change_default=True, index='btree_not_null')

    @api.depends('product_id')
    def _compute_vendor(self):
        for rec in self:
            if rec.product_id:
                supplier_line_price = self.env['product.supplierinfo'].search(
                    [('product_tmpl_id', '=', rec.product_id.id)],
                    order='price asc')
                # get name vendor
                supplier_price = supplier_line_price.mapped('name.name')
                if len(supplier_price) > 1:
                    supplier_line_delay = self.env['product.supplierinfo'].search(
                        [('product_tmpl_id', '=', rec.product_id.id)],
                        order='delay asc', limit=1)
                    supplier_delay = supplier_line_delay.mapped('name.name')
                    rec.vendors = ''.join(supplier_delay)
                else:
                     rec.vendors = ''.join(supplier_price)
