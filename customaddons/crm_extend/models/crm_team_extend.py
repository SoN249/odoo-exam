from odoo import models, api, fields


class CrmTeam(models.Model):
    _inherit = "crm.team"
    _description = "Crm sales team"
    month_1 = fields.Float('January')
    month_2 = fields.Float('February')
    month_3 = fields.Float('March')
    month_4 = fields.Float('April')
    month_5 = fields.Float('May')
    month_6 = fields.Float('June')
    month_7 = fields.Float('July')
    month_8 = fields.Float('August')
    month_9 = fields.Float('September')
    month_10 = fields.Float('October')
    month_11 = fields.Float('November')
    month_12 = fields.Float('December')

    _sql_constraints = [
        ('positive_month','CHECK(month_1>0)','Value of month 1 > 0'),
        ('positive_month2', 'CHECK(month_2>0)', 'Value of month 2 > 0'),
        ('positive_month3', 'CHECK(month_3>0)', 'Value of month 3 > 0'),
        ('positive_month4', 'CHECK(month_4>0)', 'Value of month 4 > 0'),
        ('positive_month5', 'CHECK(month_5>0)', 'Value of month 5 > 0'),
        ('positive_month6', 'CHECK(month_6>0)', 'Value of month 6 > 0'),
        ('positive_month7', 'CHECK(month_7>0)', 'Value of month 7 > 0'),
        ('positive_month8', 'CHECK(month_8>0)', 'Value of month 8 > 0'),
        ('positive_month9', 'CHECK(month_9>0)', 'Value of month 9 > 0'),
        ('positive_month10', 'CHECK(month_10>0)', 'Value of month 10 > 0'),
        ('positive_month11', 'CHECK(month_11>0)', 'Value of month 11 > 0'),
        ('positive_month12', 'CHECK(month_12>0)', 'Value of month 12 > 0'),
    ]