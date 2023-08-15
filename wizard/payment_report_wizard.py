
from odoo import models, fields, api

from datetime import date

class PaymentWizard(models.Model):
    _name = "payment.wizard"

    cliente = fields.Many2one('res.partner', string='Cliente', domain=[('is_company', '=', True)])
    fac_vencido = fields.Integer(string="FacturasVencidas", compute='_compute_cantidad_vencida')
    vencido = fields.Float(string="Cantidad Vencida", compute='_compute_cantidad_vencida', digits=(16, 0))
    pre_fac_vencido = fields.Integer(string="Facturas por vencer", compute='_compute_cantidad_vencida')
    pre_vencido = fields.Float(string="Cantidad por vencer", compute='_compute_cantidad_vencida', digits=(16, 0))
    totales = fields.Float(string="Total Deuda", compute='_compute_cantidad_vencida', digits=(16, 0))

    def action_print_report(self):
    report = self.env.ref('estadopago.action_payment_report')  # Reemplaza con el nombre correcto de tu informe
    return report.with_context(active_ids=self.ids, active_model=self._name).report_action(self)


    @api.depends('cliente')
    def _compute_cantidad_vencida(self):
        Invoice = self.env['account.invoice']
        for record in self:
            if record.cliente:
                fac_vencido = Invoice.search_count([('partner_id', '=', record.cliente.id),('type', '=', 'out_invoice'),('state', '=', 'open'),('date_due', '<=', fields.Date.today())])
                record.fac_vencido = fac_vencido
                vencido = Invoice.search([('partner_id', '=', record.cliente.id),('type', '=', 'out_invoice'),('state', '=', 'open'),('date_due', '<=', fields.Date.today())])
                total_vencido = sum(factura.amount_total for factura in vencido)
                record.vencido = total_vencido
                pre_fac_vencido = Invoice.search_count([('partner_id', '=', record.cliente.id),('type', '=', 'out_invoice'),('state', '=', 'open'),('date_due', '>', fields.Date.today())])
                record.pre_fac_vencido = pre_fac_vencido
                pre_vencido = Invoice.search([('partner_id', '=', record.cliente.id),('type', '=', 'out_invoice'),('state', '=', 'open'),('date_due', '>', fields.Date.today())])
                total_pre_vencido = sum(factura.amount_total for factura in pre_vencido)
                record.pre_vencido = total_pre_vencido
                pre_total = Invoice.search([('partner_id', '=', record.cliente.id),('type', '=', 'out_invoice'),('state', '=', 'open')])
                totales = sum(factura.amount_total for factura in pre_total)
                record.totales = totales
            else:
                record.fac_vencido = 0
                record.vencido = 0
                record.pre_fac_vencido = 0
                record.pre_vencido = 0
                record.totales = 0
        return

