{
    'name':"Purchase Extend",
    'sumamary':"Purchase",
    'description':"Long description of module's purpose",
    'category': 'Uncategorized',
    'version': '15.0',
    'depends': ['base','hr','purchase','product'],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/e_department.xml',
        'views/e_purchase_order.xml',
        'views/order_limit.xml',
        'views/employee_order_limit.xml',
        'demo/department_data.xml'
    ],
    # 'demo':[
    #     'demo/department_data.xml'
    # ]
}