{
    'name': 'merging_sale_order',
    'version': '16.0.1.0.0',
    'summary': 'merging multiple sale orders',
    'sequence': 10,
    'description': """
sale order merging
====================
This is a system that explains the complete working of commission management.
    """,
    'category': 'services',
    'depends': ['contacts', 'base', 'sale_management'],
    'data': [
        'views/sale_order.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': True,
    'license': 'LGPL-3'
}
