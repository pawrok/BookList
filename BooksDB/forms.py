from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'publication_date', 'ISBN', 'page_count', 'cover_src', 'language')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save book'))


class UpdateBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'publication_date', 'ISBN', 'page_count', 'cover_src', 'language')

    def save(self, commit=True):
        item = super(UpdateBookForm, self).save(commit=commit)
        item.code.description = self.cleaned_data['description']
        item.code.save()

    def get_initial_for_field(self, field, field_name):
        if field_name == 'description':
            return self.instance.code.description
        else:
            return super(UpdateBookForm, self).get_initial_for_field(field, field_name)
