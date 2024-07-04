# -*- coding: utf-8 -*-

from odoo import models, fields, api


# class background_required(models.Model):
#     _name = 'background_required.background_required'
#     _description = 'background_required.background_required'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
class ModelTest(models.Model):
    _name = 'model.test'
    _description = 'Тестовая модель'

    required_field_ids = fields.Many2many(
        'ir.model.fields',
        string='Обязательные поля для заполнения',
        domain=[('model', '=', 'model.test')]
    )
    char_field = fields.Char(string='Char Field')
    text_field = fields.Text(string='Text Field')
    integer_field = fields.Integer(string='Integer Field')
    float_field = fields.Float(string='Float Field')
    many2one_field = fields.Many2one('res.partner', string='Many2one Field')
    many2many_field = fields.Many2many('res.partner', string='Many2many Field')
    one2many_field = fields.One2many('related.model', 'model_test_id', string='One2many Field')


class RelatedModel(models.Model):
    _name = 'related.model'
    _description = 'Related Model for One2many Field'

    name = fields.Char(string='Название')
    model_test_id = fields.Many2one('model.test', string='Тестовая модель')
