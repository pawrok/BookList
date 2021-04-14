from django.shortcuts import redirect
from .forms import BookForm, ImportForm
from django.views.generic import CreateView, UpdateView, ListView, View, FormView, TemplateView, DeleteView
from .models import Book
from django.db.models import Q
import requests


class HomePageView(ListView):
    model = Book
    template_name = 'home.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query:
            query = ""
        return Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query) | Q(language__icontains=query)
        )


class BookCreateView(CreateView):
    template_name = 'book_form.html'
    model = Book
    form_class = BookForm
    success_url = '/home/'


class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'book_form.html'
    success_url = '/home/'


class BookImportView(FormView):
    template_name = 'import.html'
    form_class = ImportForm


class ListImportView(View):
    def get(self, request, *args, **kwargs):
        title = request.GET['title']
        author = request.GET['author']
        query = f"intitle:{title}+inauthor:{author}"
        params = {"q": query}
        books = requests.get('https://www.googleapis.com/books/v1/volumes', params=params)
        books_json = books.json()
        book_fields = self.get_fields_from_json(books_json)

        if book_fields:
            new_book = Book.objects.create(**book_fields)
            new_book.full_clean()
            new_book.save()
            return redirect("home.html")
        else:
            return redirect("import.html")

    def get_fields_from_json(self, json):
        if json.get('items'):
            first_book = json['items'][0]
        else:
            return ""

        title = first_book['volumeInfo']['title']
        author = ', '.join(first_book['volumeInfo']['authors'])
        publication_date = first_book['volumeInfo'].get('publishedDate') or ''
        isbn = list(filter(lambda book: book['type'] == 'ISBN_13', first_book['volumeInfo']['industryIdentifiers']))
        isbn = int(isbn[0].get('identifier')) if isbn else 0
        page_count = first_book['volumeInfo'].get('pageCount') or 0
        cover_src = first_book['volumeInfo'].get('imageLinks', {}).get('thumbnail') or ''
        language = first_book['volumeInfo'].get('language') or ''

        return {'title': title, 'author': author, 'publication_date': publication_date, 'ISBN': isbn,
                'page_count': page_count, 'cover_src': cover_src, 'language': language}


class InfoView(TemplateView):
    template_name = 'info.html'


class BookDeleteView(DeleteView):
    model = Book
    success_url = '/home'
    template_name = 'book_confirm_delete.html'
