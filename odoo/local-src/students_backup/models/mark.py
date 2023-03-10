from odoo import api, fields, models
from odoo.exceptions import ValidationError


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
    coeff = fields.Selection(
        string="Coefficient",
        selection=[("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5")],
        required=True,
        help="Select a coefficient in the list",
        index=True,
        default=1,
    )
    weighted_mark = fields.Float(
        string="Weighted Mark",
        compute="_get_weighted_mark",
    )

    @api.onchange("mark", "coeff")
    def _get_weighted_mark(self):
        for record in self:
            record.weighted_mark = record.mark * int(record.coeff)

    @api.constrains("mark")
    def _verify_mark(self):
        for record in self:
            if record.mark < 0 or record.mark > 20:
                raise ValidationError("Mark should be between 0 and 20")
