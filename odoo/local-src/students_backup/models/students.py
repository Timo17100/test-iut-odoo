from odoo import api, fields, models
from odoo.exceptions import ValidationError


class StudentsTraining(models.Model):
    _name = "students.training"
    _description = "Training table"
    _rec_name = "code"

    code = fields.Char(string="Training code", size=4, required=True)
    name = fields.Char(string="Training name", size=100, required=True)
    student_ids = fields.One2many(
        string="Training students",
        comodel_name="students.student",
        inverse_name="training_id",
    )

    # @api.constrains("code")
    # def _uniq_name(self):
    #     if self.env["students.training"].search_count([("code", "=", self.code)]) > 0:
    #         raise ValidationError(
    #             "Training code already exists, it must be unique")


class StudentsStudent(models.Model):
    _name = "students.student"
    _description = "Student table"
    # _rec_name = "number"

    number = fields.Char("Student number", size=11, required=True)
    firstname = fields.Char("Student firstname", size=64, required=True)
    lastname = fields.Char("Student lastname", size=64, required=True)
    training_id = fields.Many2one(
        string="Training",
        comodel_name="students.training",
        ondelete="cascade",
    )
    mark_ids = fields.One2many(
        string="Marks",
        comodel_name="students.mark",
        inverse_name="student_id",
    )
    grade_point_average = fields.Float(
        string="Grade point average",
        compute="_get_grade_point_average",
        store=True,
        index=True,
    )
    country_id = fields.Many2one(
        string="Nationality",
        comodel_name="res.country",
    )
    user_id = fields.Many2one(
        string="User",
        comodel_name="res.users",
    )

    @api.onchange("mark_ids")
    @api.depends("mark_ids")
    def _get_grade_point_average(self):
        for record in self:
            grade = 0
            if record.mark_ids:
                coeff_total = sum(int(m.coeff) for m in record.mark_ids)
                weighted_mark_total = sum(m.weighted_mark for m in record.mark_ids)
                if coeff_total != 0:
                    grade = weighted_mark_total / coeff_total
            record.grade_point_average = grade

    def name_get(self):
        result = []
        for rec in self:
            result.append((rec.id, "%s %s" % (rec.firstname, rec.lastname)))
        return result


class StudentsStudentContinuous(models.Model):
    _name = "students.student.continuous"
    _description = "Student Continuous"
    _inherit = "students.student"

    company_id = fields.Many2one(
        string="Company",
        comodel_name="res.partner",
        required=True,
    )
