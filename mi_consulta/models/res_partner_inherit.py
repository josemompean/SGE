from odoo import models, fields # type: ignore

class ResPartnerInherit(models.Model):
    _inherit = 'res.partner'

    x_is_student = fields.Boolean(string="Es Alumno en Consulta")  # Prefijo 'x_' opcional
