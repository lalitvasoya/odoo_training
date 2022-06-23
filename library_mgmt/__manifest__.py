# -*- coding: utf-8 -*-




{
    'name': "library_mgmt",
    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",
    'description': """
        Long description of module's purpose
    """,
    'author': "My Company",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/book_category_view.xml',
        'views/book_view.xml',
        'views/book_author_view.xml',
        'views/library_menu_view.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}
