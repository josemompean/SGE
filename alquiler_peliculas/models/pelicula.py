from odoo import models, fields  # type: ignore

class Pelicula(models.Model):
    _name = 'alquiler.pelicula'
    _description = 'Película'

    name = fields.Char(string='Título', required=True)
    descripcion = fields.Text(string='Descripción')
    duracion = fields.Float(string='Duración (minutos)', digits=(6, 2))
    fecha_estreno = fields.Date(string='Fecha de Estreno')
    disponible = fields.Boolean(string='Disponible', default=True)
    categoria_id = fields.Many2one('alquiler.categoria', string='Categoría')
    actor_ids = fields.Many2many('alquiler.actor', string='Actores')

    formato = fields.Selection([
        ('dvd', 'DVD'),
        ('blu-ray', 'Blu-ray'),
        ('digital', 'Digital')
    ], string='Formato', default='digital')
