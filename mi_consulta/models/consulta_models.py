from odoo import models, fields, api # type: ignore
from odoo.exceptions import ValidationError # type: ignore

class ConsultaActivity(models.Model):
    _name = 'consulta.activity'
    _description = 'Actividad o Consulta'

    name = fields.Char(string="Nombre de la Actividad", required=True)
    date = fields.Datetime(string="Fecha", default=lambda self: fields.Datetime.now(), required=True)
    price = fields.Selection(
        [('10', '10€'), ('15', '15€'), ('20', '20€')],
        string="Precio", default='10', required=True,
        help="Selecciona el precio de la actividad."
    )
    monitor = fields.Boolean(string="Monitor", compute='_compute_monitor')
    nre = fields.Char(string="NRE", required=True)

    # Relaciones
    teacher_id = fields.Many2one('consulta.teacher', string="Profesor Responsable", required=True)
    student_ids = fields.Many2many('consulta.student', string="Alumnos")

    @api.depends('price')
    def _compute_monitor(self):
        for rec in self:
            rec.monitor = (rec.price == '15')

    @api.constrains('nre')
    def _check_nre(self):
        for rec in self:
            if not rec.nre.isdigit() or len(rec.nre) < 5:
                raise ValidationError("El NRE debe contener solo dígitos y tener al menos 5 caracteres.")

class ConsultaTeacher(models.Model):
    _name = 'consulta.teacher'
    _description = 'Profesor/Responsable'

    name = fields.Char(string="Nombre del Profesor", required=True)
    activity_ids = fields.One2many('consulta.activity', 'teacher_id', string="Actividades")

class ConsultaStudent(models.Model):
    _name = 'consulta.student'
    _description = 'Alumno/Cliente/Paciente'

    name = fields.Char(string="Nombre del Alumno", required=True)
