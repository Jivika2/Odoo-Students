# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Student',
    'version': '2',
    'summary': 'Student Details',
    'sequence': 10,
    'description': """

    """,
    'website': 'https://www.jivika.com/@std',
    'depends': ['base', 'mail'],
    'data': [
        'data/wb.student.csv',
        'data/record_data.xml',
        'security/security_group.xml',
        'security/ir.model.access.csv',
        'views/view.xml',
        'wizard/set_school_wiz.xml'
    ],
    "assets": {
        "web.assets_backend": [
            "student/static/src/xml/list_controller.xml",
            "student/static/src/js/list_controller.js"
        ]
    }
}