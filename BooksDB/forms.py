from django import forms
from .models import Book

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class BookForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.field_class = 'col-sm-6'
        self.helper.label_class = 'col-sm-2'
        self.helper.add_input(Submit('submit', 'Save book'))
        self.helper.form_method = 'post'

    class Meta:
        model = Book
        fields = ('title', 'author', 'publication_date', 'ISBN', 'page_count', 'cover_src', 'language')


class ImportForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Title'}))
    author = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Author'}))

    def __init__(self, *args, **kwargs):
        super(ImportForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Import'))
        self.helper.form_method = 'get'
        self.helper.form_action = '/list'

    class Meta:
        fields = ('title', 'author')
