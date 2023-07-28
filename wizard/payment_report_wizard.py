
from odoo import models, fields, api

class PaymentWizard(models.Model):
    _name = "payment.wizard"
    _inherit = 'res.partner'

    date = fields.Date(default=fields.Date.today, required=True)
    cliente = fields.Many2one('res.partner', string='Cliente', domain=[('is_company', '=', True)])
    fac_vencido = fields.Integer(string="FacturasVencidas", compute='_compute_cantidad_vencida')
    vencido = fields.Float(string="Cantidad Vencida", compute='_compute_cantidad_vencida')

    def name_get(self):
        result = []
        for partner in self:
            name = partner.name  # Mostrar el campo 'name' en lugar de 'display_name'
            result.append((partner.id, name))
        return result

    def action_print_report(self):
        data = {}
        #data['form'] = v
        data['ids'] = self.env.context.get('active_ids', [])
        data['model'] = self.env.context.get('active_model', 'payment.wizard')
        data['date'] = self.date
        data['cliente'] = self.cliente
        data['fac_vencido'] = self.cliente
        return self.env.ref('payment_report.action_payment_report').report_action(self, data=data)

    @api.depends('cliente')
    def _compute_cantidad_vencida(self):
        Invoice = self.env['account.invoice']
        for record in self:
            if record.cliente:
                facturas_vencidas = Invoice.search_count([('partner_id', '=', record.cliente.id),('type', '=', 'out_invoice'),('state', '=', 'open')])
                total_vencido = sum(factura.amount_total for factura in facturas_vencidas)
                record.fac_vencido = fac_vencido
                record.vencido = total_vencido
            else:
                record.fac_vencido = 0
                record.vencido = 0
        return
