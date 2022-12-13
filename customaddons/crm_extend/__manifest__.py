{
    'name': "CRM Extend",
    'summary': "Manage my crm",
    'depends': ['base','crm','sale'],
    'version': '15.0.1',
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/crm_extend_views.xml',
        'views/crm_extend_team.xml',
        'views/e_sale_order.xml',
        'views/plan_sales_order.xml',
        'views/indicator_evaluation.xml',
        'wizard/report_detail.xml',
        'wizard/report_indicator_evaluation.xml',
    ]
}