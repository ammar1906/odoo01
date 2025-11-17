{
    'name': "TrainDZ - Government Training Management",
    'summary': "Module to manage public engagement, training courses, and related finances for a government body.",
    'version': '1.0',
    'sequence': 1,
    'category': 'Government/Training',

    # 👤 Author & Website Info
    'author': "madday",


    'depends': [
        'base','sale'

    ],

    'data': [
        "views/users_views.xml",

        "views/tools_views.xml",
        "views/sale_order_views.xml",






        "views/menus_views.xml",

    ],


    'application': True,  # Set to True if this is a standalone business application
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',  # Recommended open source license for Odoo modules
}