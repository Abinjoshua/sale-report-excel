# -*- coding: utf-8 -*-
{
    'name': "Sale Report Excel",
    'version': "1.0",
    'licence': "LGPL-3",
    'author': "Cybrosys",
    'website': "http://www.cybrosys.com",
    'sequence': 1,
    'application': True,
    'depends': ['sale'],
    'data': ['views/sale_report_excel_views.xml'],
    'auto_install': True,
    'assets': {
        'web.assets_backend': [
            'sale_report_excel/static/src/js/action_manager.js']}
}
