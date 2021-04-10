from django import forms
from .models import Book

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column


class BookForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.field_class = 'col-sm-6'
        self.helper.label_class = 'col-sm-2'
        # self.helper.layout = Layout(
        #     Row(
        #         Column('title', css_class='form-group col-md-6 mb-0'),
        #         Column('author', css_class='form-group col-md-6 mb-0'),
        #         css_class='form-row'
        #     ),
        #     'publication_date',
        #     'ISBN',
        #     'page_count',
        #     'cover_src',
        #     'language'
        # )

    class Meta:
        model = Book
        fields = ('title', 'author', 'publication_date', 'ISBN', 'page_count', 'cover_src', 'language')
