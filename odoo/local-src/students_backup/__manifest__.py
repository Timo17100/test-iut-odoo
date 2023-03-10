{
    "name": "Gestion des étudiants",
    "version": "2.0",
    "category": "Generic Modules/Others",
    "description": """Test création module gestion des étudiants Odoo v14""",
    "author": "Moi",
    "depends": ["base"],
    "data": [
        "security/students_security.xml",
        "security/ir.model.access.csv",
        "data/students_training_data.xml",
        "data/students_student_data.xml",
        "views/students_views.xml",
        "views/training_views.xml",
        "views/mark_views.xml",
        "views/menu_views.xml",
        "views/res_partner_views.xml",
        "reports/students_report.xml",
    ],
    "demo": [
        "demo/students_student_demo.xml",
        # "demo/students_mark_demo.xml",
    ],
    "installable": True,
    "auto_install": False,
}
