# -*- coding: utf-8 -*-

from odoo import api, models, _
from odoo.exceptions import UserError

import time
import logging
from datetime import timedelta, datetime

_logger = logging.getLogger(__name__)


class ReportPayment(models.AbstractModel):
	_name = 'report.payment_report.report_payment'
	_description = 'Payment Report'

	@api.model
	def _get_report_values(self, docids, data=None):
		res = {}
		model = self.env.context.get('active_model')
		docs = self.env[model].browse(self.env.context.get('active_id'))

		selected_date = data.get("date")
		selected_date = datetime.strptime(selected_date, "%Y-%m-%d").date()

		payments = self.env["account.payment"].search([("payment_date","=",selected_date)])
		t_payments = payments.filtered(lambda r: selected_date in r.reconciled_invoice_ids.mapped("date_invoice"))
		y_payments = payments.filtered(lambda r: selected_date not in r.reconciled_invoice_ids.mapped("date_invoice"))

		return {
			'doc_ids': docids,
			'doc_model': model,
			'data': data,
			'docs': docs,
			'time': time,
			't_payments': t_payments,
			'y_payments': y_payments,
			'payments': payments,
		}
