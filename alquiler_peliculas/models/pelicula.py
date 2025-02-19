from odoo import models, fields, api # type: ignore
from odoo.exceptions import ValidationError  # type: ignore 
class Pelicula(models.Model):
    _name = 'alquiler.pelicula'
    _description = 'Película'

    name = fields.Char(
        string='Título', 
        required=True, 
        help="Introduce el título de la película."
    )
    descripcion = fields.Text(
        string='Descripción',
        help="Descripción general de la película."
    )
    duracion = fields.Float(
        string='Duración (minutos)',
        digits=(6, 2),
        required=True,
        help="Duración en minutos. Debe ser mayor que 0."
    )
    fecha_estreno = fields.Date(
        string='Fecha de Estreno',
        required=True,
        help="Fecha en la que se estrenó la película."
    )
    disponible = fields.Boolean(
        string='Disponible',
        default=True,
        help="Indica si la película está disponible para alquiler."
    )
    categoria_id = fields.Many2one(
        'alquiler.categoria',
        string='Categoría',
        required=True,
        help="Selecciona la categoría a la que pertenece la película."
    )
    actor_ids = fields.Many2many(
        'alquiler.actor',
        string='Actores',
        help="Selecciona los actores que participan en la película."
    )

    formato = fields.Selection([
        ('dvd', 'DVD'),
        ('blu-ray', 'Blu-ray'),
        ('digital', 'Digital')
    ], 
        string='Formato', 
        default='digital',
        required=True,
        help="Selecciona el formato en el que está disponible la película."
    )

    @api.constrains('duracion')
    def _check_duracion(self):
        """ Validación para asegurarse de que la duración sea mayor que 0. """
        for record in self:
            if record.duracion <= 0:
                raise ValidationError("La duración debe ser mayor que 0 minutos.")
