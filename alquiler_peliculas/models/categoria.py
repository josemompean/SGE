from odoo import models, fields # type: ignore

class Categoria(models.Model):
    _name = 'alquiler.categoria'
    _description = 'Categoría'

    name = fields.Char(string='Nombre', required=True)
    descripcion = fields.Text(string='Descripción')
    pelicula_ids = fields.One2many('alquiler.pelicula', 'categoria_id', string='Películas')