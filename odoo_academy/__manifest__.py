{
    'name': 'Oddo Academy',
    
    'summary': """Academy app to manage Training""",
    
    'description': """
        Academy Module to manage Training:
        - Courses
        - Sessions
        - Attendees
    """,
    
    'author':'Odoo',
    
    'website': 'https://www.test.com',
    
    'category': 'Training',
    'license': 'OPL-1',
    'version': '0.1',
    'depends': ['base'], 
    
    'data': [
        'security/academy_security.xml',
        'security/ir.model.access.csv',
        'views/academy_menuitems.xml',
        'views/course_views.xml',
        'views/session_views.xml',
    ],
    'demo': [
        'demo/academy_demo.xml',
        
    ],
}