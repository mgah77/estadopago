
from odoo import models, fields



class PaymentWizard(models.Model):
    _name = "payment.wizard"
    _inherit = 'res.partner'

    date = fields.Date(default=fields.Date.today, required=True)
    cliente = fields.Many2one('res.partner', string='Cliente', domain=[('is_company', '=', True)])

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

        return self.env.ref('payment_report.action_payment_report').report_action(self, data=data)
