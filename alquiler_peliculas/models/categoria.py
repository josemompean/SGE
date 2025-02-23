from odoo import models, fields  # type: ignore

class Categoria(models.Model):
    _name = 'alquiler.categoria'
    _description = 'Categoría de Película'

    name = fields.Char(
        string="Nombre",
        required=True,
        help="Nombre de la categoría de película."
    )
    descripcion = fields.Text(
        string="Descripción",
        help="Descripción de la categoría de película."
    )
    pelicula_ids = fields.One2many(
        'alquiler.pelicula', 'categoria_id',
        string="Películas",
        help="Películas que pertenecen a esta categoría."
    )

    _sql_constraints = [
        ('unique_categoria_name', 'unique(name)', "El nombre de la categoría debe ser único."),
    ]
