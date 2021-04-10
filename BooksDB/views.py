from django.shortcuts import render
from django.shortcuts import HttpResponse
from .forms import BookForm
from django.views.generic import FormView
from django.views.generic.base import TemplateView
from django.views.generic import CreateView, UpdateView, ListView
from .models import Book
from django.db.models import Q
from django.urls import reverse_lazy


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


class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'book_form.html'

    def get_success_url(self):
        return reverse_lazy('item-detail', kwargs={'pk': 1})
