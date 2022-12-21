{
    'name': "Api Report",
    'summary': "My api",
    'depends': ['base','crm_extend','purchase_extend','mail'],
    'version': '15.0.1',
    'data': [
        'security/ir.model.access.csv',
        'views/department_cronjob.xml',
        'views/indicator_evaluation_cronjob.xml',
        'views/purchase_cronjob.xml',
        'data/sale_purchase_email_template.xml',
        'data/scheduled_action.xml'
    ]
}