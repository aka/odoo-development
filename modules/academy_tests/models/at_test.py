# -*- coding: utf-8 -*-
#pylint: disable=I0011,W0212,E0611,C0103,R0903,C0111
###############################################################################
#    License, author and contributors information in:                         #
#    __openerp__.py file at the root folder of this module.                   #
###############################################################################

from openerp import models, fields, api
from openerp.tools.translate import _
from logging import getLogger


_logger = getLogger(__name__)


class AtTest(models.Model):
    """ Stored tests which can be reused in future

    Fields:
      name (Char): Human readable name which will identify each record.

    """

    _name = 'at.test'
    _description = u'Stored tests which can be reused in future'

    _rec_name = 'name'
    _order = 'name ASC'

    _inherit = ['mail.thread']

    name = fields.Char(
        string='Name',
        required=True,
        readonly=False,
        index=True,
        default=None,
        help="Name for this text",
        size=50,
        translate=True,
        track_visibility='onchange'
    )

    description = fields.Text(
        string='Description',
        required=False,
        readonly=False,
        index=False,
        default=None,
        help='Something about this test',
        translate=True
    )
