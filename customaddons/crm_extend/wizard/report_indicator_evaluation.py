from odoo import fields, models, api, _
from datetime import date


class ReportIndicatorEvaluation(models.Model):
    _name = 'report.indicator.evaluation'
    month = fields.Selection([
        ('0', date.today().strftime('%B')),
        ('1', 'January'),
        ('2', 'February'),
        ('3', 'March'),
        ('4', 'April'),
        ('5','May'),
        ('6', 'June'),
        ('7', 'July'),
        ('8', 'August'),
        ('9', 'September'),
        ('10', 'October'),
        ('11', 'November'),
        ('12', 'December')
    ], required="True", default='0')
    sale_team = fields.Many2many('crm.team', string="Sale team")

    def btn_confirm(self):
        if self.month and self.sale_team:
            if self.month == '0':
                self.month = str(date.today().month)
            sale_teams_id = self.sale_team.mapped('id')
            self.env['indicator.evaluation'].sudo().search([]).unlink()
            for id in sale_teams_id:
                self.env['indicator.evaluation'].sudo().create({
                    'sale_team': id,
                    'month': int(self.month)
                })
            context = {
                'name': _("Report Indicator Evaluation"),
                'view_mode': 'tree',
                'res_model': 'indicator.evaluation',
                'type': 'ir.actions.act_window',
                'view_id': self.env.ref('crm_extend.indicator_evaluation_view_tree').id,
                'target': 'current',
                'domain': [('sale_team', 'in', sale_teams_id), ('create_month', '=', self.month)],
                'context': {'create': False, 'edit': False, 'delete': False}
            }
        else:
            context = {
                'name': _("Report Indicator Evaluation"),
                'view_mode': 'tree',
                'res_model': 'indicator.evaluation',
                'type': 'ir.actions.act_window',
                'view_id': self.env.ref('crm_extend.indicator_evaluation_view_tree').id,
                'target': 'current',
                'context': {'create': False, 'edit': False, 'delete': False}
            }
        return context



