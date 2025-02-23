{
    'name': 'Mi Consulta',
    'version': '1.0',
    'depends': ['base', 'contacts'],
    'author': 'José Mompeán Roca',
    'category': 'Gestión',
    'sequence': 1,
    'summary': 'Sistema de gestión de consultas',
    'description': 'Este módulo permite gestionar consultas',
    'license': 'LGPL-3',  # Se agrega la licencia
    'data': [
        'views/consulta_views.xml',
        'views/menus.xml',
        'views/res_partner_inherit_views.xml',
        'report/consulta_report.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/demo_data.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}


