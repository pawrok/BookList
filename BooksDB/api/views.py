from django.db.models import Q
from .serializers import BookSerializer
from rest_framework import permissions
from BooksDB.models import Book
from rest_framework.generics import ListAPIView
import re


class BookViewSet(ListAPIView):
    """
    API endpoint that allows books to be viewed or edited.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # to require permissions change below to [permissions.IsAuthenticated]
    permission_classes = (permissions.AllowAny,)
    http_method_names = ['get']

    def get_queryset(self):
        queryset = Book.objects.all()
        query = self.request.META['QUERY_STRING']

        if not query:
            query = ""

        title_q = re.search(r"(?<=intitle:)\w+", query)
        title_q = title_q.group(0) if title_q else ''

        author_q = re.search(r"(?<=inauthor:)\w+", query)
        author_q = author_q.group(0) if author_q else ''

        queryset = queryset.filter(
            Q(title__icontains=title_q) & Q(author__icontains=author_q)
            )

        return queryset
