# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2001-2014 Zhuhai sunlight software development co.,ltd. All Rights Reserved.
#    Author: Kenny
#    Website: http://zhsunlight.cn
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#
##############################################################################

{
    'name': 'Paypal Payment (Sandbox)',
    'description': """
This is a test payment via paypal sandbox
===============================================
    """,
    'author': 'Sunlight Software',
    'version': '1.0',
    'category': 'Sale Management',
    'website': 'http://zhsunlight.cn',
    'installable': True,
    'depends': [
        'payment_paypal',
    ],
    'data': [
        'payment_paypal_sandbox_data.xml',
    ],
}
