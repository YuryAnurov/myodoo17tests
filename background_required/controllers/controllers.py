# -*- coding: utf-8 -*-
# from odoo import http


# class BackgroundRequired(http.Controller):
#     @http.route('/background_required/background_required', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/background_required/background_required/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('background_required.listing', {
#             'root': '/background_required/background_required',
#             'objects': http.request.env['background_required.background_required'].search([]),
#         })

#     @http.route('/background_required/background_required/objects/<model("background_required.background_required"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('background_required.object', {
#             'object': obj
#         })
