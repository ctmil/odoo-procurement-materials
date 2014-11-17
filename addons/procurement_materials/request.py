# -*- coding: utf-8 -*-
from openerp import netsvc
from openerp.osv import osv, fields
from openerp.tools.translate import _

class request(osv.osv):
    """"""
    
    _name = 'procurement_materials.request'
    _description = 'request'

    _states_ = [
        # State machine: untitle
        ('draft','Draft'),
        ('confirmed','Confirmed'),
        ('in_progress','In Progress'),
        ('done','Done'),
        ('cancelled','Cancelled'),
    ]

    _columns = {
       'user_id': fields.many2one('res.users', string=_('user_id')),
       'section_id': fields.many2one('sale.case.section', string=_('section_id')),
       'date_planned': fields.date(string=_('date_planned')),
       'state': fields.selection(_states_, "State"),
       'line_ids': fields.one2many('procurement_materials.request_line', 'request_id', string=_('line_ids')),
    }

    _defaults = {
        'state': 'draft',
    }

    _constraints = [
    ]

    def do_process(self, cr, uid, ids, context=None):
        """"""
        raise NotImplementedError

request()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
