# -*- coding: utf-8 -*-
{
    'name': 'Background Required Widget',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Custom widget to change background color of required fields.',
    'depends': ['base', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    # 'assets': {
    #     'web.assets_backend': [
    #         'background_required/static/src/js/background_required_widget.js',
    #     ],
    # },
    'installable': True,
    'application': False,
}
