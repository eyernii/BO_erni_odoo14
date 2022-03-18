# -*- coding: utf-8 -*-
# from odoo import http


# class BookingOrderErniOdoo14(http.Controller):
#     @http.route('/booking_order_erni_odoo14/booking_order_erni_odoo14/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/booking_order_erni_odoo14/booking_order_erni_odoo14/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('booking_order_erni_odoo14.listing', {
#             'root': '/booking_order_erni_odoo14/booking_order_erni_odoo14',
#             'objects': http.request.env['booking_order_erni_odoo14.booking_order_erni_odoo14'].search([]),
#         })

#     @http.route('/booking_order_erni_odoo14/booking_order_erni_odoo14/objects/<model("booking_order_erni_odoo14.booking_order_erni_odoo14"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('booking_order_erni_odoo14.object', {
#             'object': obj
#         })
