# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Book(models.Model):
    _name = 'book'
    _description = 'library_management'

    name = fields.Char(size=255)
    category = fields.Selection([('literary-fiction', 'Literary Fiction'), ('novel', 'Novel'), ('compute-science', 'Computer Science')])
    isbn = fields.Integer()
    title = fields.Char(size=255)
    publisher = fields.Char(size=255)
    copyright = fields.Char(size=255)
    edition = fields.Char(size=255)
    author = fields.Char(size=255)
    price = fields.Integer()
    pages = fields.Integer()
