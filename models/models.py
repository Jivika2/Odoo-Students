from odoo import fields, models


class School(models.Model):
    _name = "wb.school"
    _description = "School"
    

    name = fields.Char("School Name")
    student_list = fields.One2many("wb.student", "school_id",
                                   string="Student List")
    password = fields.Char("Password")


class Student(models.Model):
    _name = "wb.student"
    _description = "Student profile"
    _order = "name desc"

    seq = fields.Integer("Sequence", default=10)
    name = fields.Char("Student Name")
    fees = fields.Integer("Fees")
    school_id = fields.Many2one("wb.school", "School")
    

   
