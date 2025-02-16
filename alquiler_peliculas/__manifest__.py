{
    'name': 'Alquiler de Películas',
    'version': '1.0',
    'depends': ['base', 'contacts'],  
    'author': 'José Mompeán Roca',
    'category': 'Gestión',
    'sequence': 1, 
    'summary': 'Sistema de gestión de alquiler de películas',
    'description': 'Este módulo permite gestionar películas, actores y categorías para un sistema de alquiler.',
    'data': [
        'views/pelicula_views.xml',  
        "views/categoria_views.xml",
        "views/actor_views.xml"
        'views/menu.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}

