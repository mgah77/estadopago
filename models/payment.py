# -*- coding: utf-8 -*-

from odoo import api, models, _, fields


class AccountPayment(models.Model):
    _inherit = 'account.payment'

    def _get_filter_amount(self, payment_form):
        self.ensure_one()
        if hasattr(self, "payment_form"):
            if self.payment_form == payment_form:
                return self.amount
            else:
                return 0
        else:
            return 0

    @api.multi
    def _get_filter_total_amount(self, payment_form):
        result = 0
        payments = self
        if payments and hasattr(payments[0], "payment_form"):
            result = sum(payments.filtered(lambda r: r.payment_form == payment_form).mapped("amount"))
        return result

    def _get_date(self):
        self.ensure_one()
        return [x.strftime("%Y-%m-%d") for x in self.mapped("reconciled_invoice_ids.date_invoice")]
