# -*- coding: utf-8 -*-

from odoo import api, models, _
from odoo.exceptions import UserError

import time
import logging
from datetime import timedelta, datetime

_logger = logging.getLogger(__name__)


class ReportEstadoPago(models.AbstractModel):
	_name = 'report.payment_report.estado_pago'
	_description = 'Payment Report'

