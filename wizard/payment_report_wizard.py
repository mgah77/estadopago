
from odoo import models, fields



class PaymentWizard(models.Model):
    _name = "payment.wizard"

    date = fields.Date(default=fields.Date.today, required=True)


    def action_print_report(self):
        data = {}
        #data['form'] = v
        data['ids'] = self.env.context.get('active_ids', [])
        data['model'] = self.env.context.get('active_model', 'payment.wizard')
        data['date'] = self.date

        return self.env.ref('tj_payment_report.action_payment_report').report_action(self, data=data)
