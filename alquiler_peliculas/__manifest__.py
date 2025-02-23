{
    'name': 'Alquiler de Películas',
    'version': '1.0',
    'depends': ['base'],
    'author': 'José Mompeán Roca',
    'category': 'Gestión',
    'summary': 'Sistema de gestión de alquiler de películas',
    'description': 'Este módulo permite gestionar películas, actores y categorías para un sistema de alquiler.',
    'data': [
        'security/ir.model.access.csv',
        'views/pelicula_views.xml',
        'views/categoria_views.xml',
        'views/actor_views.xml',
        'views/menu.xml',
        'data/datos_ejemplo.xml'
    ],
    'installable': True,
    'application': True
}
