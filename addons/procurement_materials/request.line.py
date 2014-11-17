# -*- coding: utf-8 -*-
from openerp import netsvc
from openerp.osv import osv, fields
from openerp.tools.translate import _

class request.line(osv.osv):
    """"""
    
    _name = 'procurement_materials.request.line'
    _description = 'request.line'

    _columns = {
       'product_id': fields.many2one('product.product', string=_('product_id')),
       'product_qty': fields.float(string=_('product_qty')),
       'product_uom': fields.many2one('product.uom', string=_('product_uom')),
       'request_id': fields.many2one('procurement_materials.request', string=_('request_id'),required=True), 
    }

    _defaults = {
        'request_id': lambda self, cr, uid, context=None: context and context.get('request_id', False),
    }

    _constraints = [
    ]

request.line()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
