{
    "name": "Gestion des étudiants",
    "version": "0.5",
    "category": "Generic Modules/Others",
    "description": """Test création module gestion des étudiants Odoo v14""",
    "author": "Moi",
    "depends": ["base"],
    "data": [
"data/students_training_data.xml",
        "data/students_student_data.xml",
        "views/students_views.xml",
        "views/training_views.xml",
        "views/mark_views.xml",
        "views/menu_views.xml",
    ],
    "installable": True,
    "auto_install": False,
}
