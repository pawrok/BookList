from rest_framework import serializers
from BooksDB.models import Book


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'author', 'publication_date', 'ISBN', 'page_count', 'cover_src', 'language')
