{
    'name': 'Customer Name: Task Description',
    'summary': 'Summary of task',
    'description': '''
        Long description of module's purpose
    ''',

    'category': 'Customizations',
    'website': 'https://www.odoo.com',
    'author': 'Odoo, Inc',
    'version': '1.0',
    'license': 'OPL-1',

    # change the module name as per the requirements
    'depends': ['base'],
    'data': [
        # security
        # 'security/ir.model.access.csv',

        # views
        # 'views/views.xml',

        # reports
        # 'report/report_views.xml',
    ],
    'demo': [
        # if demo data requried
        # 'data/demo.xml',
    ],

     # remove this lines if not needed
    'assets': {
        'web.assets_frontend': [],
        'web.assets_backend': [],
        'web.assets_common': [],
    },

    'installable': True,
    'application': False,
    'auto_install': False,
}
