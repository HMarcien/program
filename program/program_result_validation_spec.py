# -*- coding: utf-8 -*-

##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2014 Savoir-faire Linux (<www.savoirfairelinux.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.osv import fields, orm
from openerp.tools.translate import _


class program_result_validation_spec(orm.Model):

    _name = 'program.result.validation.spec'
    _description = 'Result Validation Specifications'
    _columns = {
        'level_id': fields.many2one(
            'program.result.level',
            'Level',
            ondelete='cascade',
            required=True,
        ),
        'group_id': fields.many2one(
            'res.groups',
            'Group',
            ondelete='cascade',
            required=True
        ),
        'states': fields.char(
            'States',
            required=True,
            help='Comma separated list of states which can be validated with '
                 'group'
        ),
    }
    _sql_constraints = [
        ('unique_level_group', 'UNIQUE(level_id, group_id)',
         lambda self, *a, **kw: self._unique_msg(*a, **kw)),
    ]

    @staticmethod
    def _unique_msg(cr, uid, ids, context=None):
        return _('Duplicate Group')

    def get_all_states(self, cr, uid, context=None):
        ids = self.search(cr, uid, [], context=context)
        states = self.read(cr, uid, ids, ['states'], context=context)
        res = []
        for state in states:
            if state['states']:
                res += state['states'].split(',')
        return res
