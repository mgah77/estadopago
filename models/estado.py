from odoo import models, fields, api, _
from odoo.exceptions import ValidationError




    #@api.model
    #def create(self,vals):
    #    if vals.get('name','New')=='New':
    #        vals['name']=self.env['ir.sequence'].next_by_code('pre.estado') or 'New'
    #    result = super(ImportTemplate,self).create(vals)
    #    return result