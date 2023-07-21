{
    'name':'Addon Estado de Pagos',
    'version':'1.0',
    'category':'General',
    'summary': '',
    'description': """
    Addon

    Estado de pago de clientes


       """,
    'author' : 'M.Gah',
    'website': '',
    'installable': True,
    'auto_install': False,
    'application': True,
    'depends': ['base','sale','account'],
    'data': [
            'security/groups.xml',
            'security/ir.model.access.csv',
            'views/estado.xml',
            ],
}