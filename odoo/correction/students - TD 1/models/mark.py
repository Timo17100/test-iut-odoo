from odoo import fields, models


class StudentsMark(models.Model):
    _name = "students.mark"
    _description = "Students Mark"

    subject = fields.Char(
        string="Subject",
        required=True,
    )
    mark = fields.Float(
        string="Mark",
        required=True,
    )
    student_id = fields.Many2one(
        string="Student",
        comodel_name="students.student",
        required=True,
    )
