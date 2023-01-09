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
                # get list id of supplier with price ascending
                supplier_line_price = self.env['product.supplierinfo'].search(
                    [('product_tmpl_id', '=', rec.product_id.id)],
                    order='price asc')
                # get name supplier
                supplier_price = supplier_line_price.mapped('name.name')
                # Check if many supplier have same price then check delay of supplier
                if len(supplier_price) > 1:
                    # Get list delay of supplier
                    supplier_line_delay = self.env['product.supplierinfo'].search(
                        [('product_tmpl_id', '=', rec.product_id.id)],
                        order='delay asc', limit=1)
                    supplier_delay = supplier_line_delay.mapped('name.name')
                    rec.vendors = ''.join(supplier_delay)
                else:
                     rec.vendors = ''.join(supplier_price)
