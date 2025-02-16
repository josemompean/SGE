from odoo import models, fields # type: ignore

class Actor(models.Model):
    _name = 'alquiler.actor'
    _description = 'Actor'

    name = fields.Char(string='Nombre', required=True)
    fecha_nacimiento = fields.Date(string='Fecha de Nacimiento')
    nacionalidad = fields.Char(string='Nacionalidad')
    pelicula_ids = fields.Many2many('alquiler.pelicula', string='Películas')