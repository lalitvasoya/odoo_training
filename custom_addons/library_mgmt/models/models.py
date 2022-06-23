# -*- coding: utf-8 -*-

# from pyexpat import model
from odoo import models, fields, api


class BookCategory(models.Model):
    _name = "book.category"
    _description = "Book category"
    _rec_name = "book_name"

    book_name = fields.Char()
    color = fields.Integer()


class BookAuthor(models.Model):
    _name = "book.author"
    _description = "Book Author"
    
    name = fields.Char()
    book_ids = fields.One2many('book', 'author_id')


class Book(models.Model):
    _name = 'book'
    _description = 'library_management'

    name = fields.Char(size=255)
    isbn = fields.Integer()
    title = fields.Char(size=255)
    publisher = fields.Char(size=255)
    copyright = fields.Char(size=255)
    edition = fields.Char(size=255)
    author_id = fields.Many2one('book.author')
    price = fields.Integer()
    pages = fields.Integer()
    category_ids = fields.Many2many('book.category', 'book_book_category_relationships', 'book_id', 'book_category_id')
    primary_category_ids = fields.Many2many('book.category', 'book_book_category_relationships_primary', 'book_id', 'book_category_id')
