from odoo import models, fields, api
from odoo.exceptions import ValidationError


class BookCategory(models.Model):
    _name = "book.category"
    _description = "Book category"
    _rec_name = "book_name"

    book_name = fields.Char()
    color = fields.Integer()

    @api.model_create_multi
    def create(self, vals_list):
        
        for vals in vals_list:
            if self.search_count([('book_name', '=', vals.get('book_name'))]):
                raise ValidationError('Category with this name already exists!')

        res = super().create(vals_list)
        return res

    def write(self, vals):
        if vals.get('book_name'):
            if self.search_count([('book_name', '=', vals.get('book_name'))]):
                raise ValidationError('Category with this name already exists!')
        return super().write(vals)


class BookAuthor(models.Model):
    _name = "book.author"
    _description = "Book Author"
    
    name = fields.Char()
    about = fields.Char()
    book_ids = fields.One2many('book', 'author_id')
    count = fields.Integer(compute='_compute_total_book')

    @api.depends('book_ids')
    def _compute_total_book(self):
        self.count = len(self.book_ids)
    
    @api.constrains('about')
    def _check_length(self):
        for book in self:
            if len(book.about.strip())<10:
                raise ValidationError('Description Should be grater than 10 character')


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
    about = fields.Char(related='author_id.about')


    @api.onchange("name")
    def _onchange_edition(self):
        self.title = "Title " + (self.name or '')

    @api.ondelete(at_uninstall=False)
    def _check_has_selected_category(self):
        if self.author_id:
            raise ValidationError("You can not delete books. Books link to the author")

    def unlink(self):
        for book in self:
            book.category_ids.unlink()
        return super().unlink()

    def copy(self, default={}):
        if 'name' not in default:
            default['name'] = "%s (Copy)".format(self.name)
        return super().copy(default=default)
