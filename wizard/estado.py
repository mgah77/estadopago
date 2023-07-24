from odoo import models, fields, api


class Estado_pago(models.TransientModel):
    _name = 'estadopago'
    _descryption = 'Estado de pago de clientes'

    consulta = fields.Char(string="nro consulta")
    fecha = fields.Date(string="fecha")
    us_id = fields.Integer(string="Usuario")
    credito = fields.Float(string="Credito")
    fac_vencido = fields.Integer(string="FacturasVencidas")
    vencido = fields.Float(string="Cantidad Vencida")
    pre_fac_vencido = fields.Integer(string="Facturas por vencer")
    pre_vencido = fields.Float(string="Cantidad por vencer")
    total = fields.Float(string="Total Deuda")