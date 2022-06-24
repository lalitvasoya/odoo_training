# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = "sale.order"

    extended_custom_order = fields.Char("extended custom order")


    @api.model
    def default_get(self, fields):
        res = super().default_get(fields)
        res["extended_custom_order"] = "Not assign"
        return res

    @api.onchange('partner_id')
    def _onchange_parter_id(self):
        self.extended_custom_order = "custom"

    def action_cancel(self):
        for order in self:
            if order.extended_custom_order:
                raise ValidationError('action_cancel')
        return super().action_cancel()
