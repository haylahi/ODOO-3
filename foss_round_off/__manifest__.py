# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Round Off Invoice Amount',
    'version': '1.0',
    'summary': 'Rounding of Invoice Amount',
    'description': 'This module is to round the invoice (decimal amount) to the nearest value for Customer Invoice and Vendor Bills',
    'category': 'Accounting',
    'author': 'Foss Infotech Private Limited',
    'website': "www.fossinfotech.com",
    'company': 'Foss Infotech Private Limited',
    'depends': ['base', 'account'],
    'data': [
        'views/round_off_view.xml',
        'views/res_config_settings_views.xml',
    ],
    'images': [],
    'installable': True,
    'auto_install': False,
    'application': False,
}