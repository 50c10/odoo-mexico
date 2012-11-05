#!/usr/bin/python
# -*- encoding: utf-8 -*-
###########################################################################
#    Module Writen to OpenERP, Open Source Management Solution
#    Copyright (C) Vauxoo (<http://vauxoo.com>).
#    All Rights Reserved
###############Credits######################################################
#    Coded by: Carlos Funes(juan@vauxoo.com)
#############################################################################
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
################################################################################
from osv import fields, osv, orm

class account_tax_category(osv.osv):
    _name='account.tax.category'
    
    _columns = {
        'company_id': fields.many2one('res.company', 'Company', required=True),
        'name': fields.char('Name', size=64, required=True),
        'code': fields.char('Code', size=32, required=True),
        'active': fields.boolean('Active'),
        'sign': fields.integer('Sign'),
        'category_ids': fields.one2many('account.tax', 'tax_category_id', 'Category'),
        
    }
    
    _defaults = {
    'active': 1,
    'company_id': lambda s, cr, uid, c: s.pool.get('res.company')._company_default_get(cr, uid, 'account.tax.category', context=c),
    }
    
account_tax_category()

class account_tax(osv.osv):
    _inherit = 'account.tax'

    _columns = {
        'tax_category_id': fields.many2one('account.tax.category','Tax Category',required=False),
    }

account_tax()
