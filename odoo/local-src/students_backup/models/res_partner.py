from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    student_continuous_ids = fields.One2many(
        string="Continuous Students",
        comodel_name="students.student.continuous",
        inverse_name="company_id",
    )
