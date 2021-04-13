from django.shortcuts import render
from django.shortcuts import HttpResponse
from .forms import BookForm, ImportForm
from django.views.generic import FormView
from django.views.generic.base import TemplateView
from django.views.generic import CreateView, UpdateView, ListView, View
from .models import Book
from django.db.models import Q
from django.urls import reverse_lazy
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
    # def get_queryset(self):
    #     print(self.request)
    #     # FormView.get_queryset()


class ListImportView(View):
    books = None

    def get(self, request, *args, **kwargs):
        title = request.GET['title']
        author = request.GET['author']
        query = f"intitle:{title}+inauthor:{author}"
        params = {"q": query}
        self.books = requests.get('https://www.googleapis.com/books/v1/volumes', params=params)
        self.books = self.books.json()
        context = {'books': self.books}
        return render(request, "list.html", context=context)

    def post(self, request, *args, **kwargs):
        index = request.POST.get('index')
        unpack_data = self.books[index]
        book = Book(*unpack_data)
        # if book.is_valid():
        #     book.save()
            # return Response(serializer.data, status=status.HTTP_201_CREATED)
