# -*- coding: utf-8 -*-
{
    'name': 'Addon Estado Pagos',
    'version': '1.0',
    'category': 'Accounting',
    'summary': 'print pdf report of payment for a particular date',
    'website': '',
    'author': 'mgah',
    'depends': ['account'],
    'data': [
        'security/ir.model.access.csv',
        'security/groups.xml',
        'report/report_action.xml',
        'wizard/payment_report_wizard_view.xml',
        'report/report_payment.xml',        
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
