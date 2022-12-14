# -*- coding: utf-8 -*-
# from odoo import http


# class ApiReport(http.Controller):
#     @http.route('/api_report/api_report', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/api_report/api_report/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('api_report.listing', {
#             'root': '/api_report/api_report',
#             'objects': http.request.env['api_report.api_report'].search([]),
#         })

#     @http.route('/api_report/api_report/objects/<model("api_report.api_report"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('api_report.object', {
#             'object': obj
#         })
