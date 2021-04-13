from django.test import TestCase, Client, RequestFactory
import unittest
from .models import Book
from django.urls import reverse
from .views import ListImportView
from .api.serializers import BookSerializer
from rest_framework import status
from json import dumps, loads


class BookListViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    @classmethod
    def setUpTestData(cls):
        number_of_books = 11

        for book_id in range(number_of_books):
            Book.objects.create(
                title=f'Title {book_id}',
                author=f'book {book_id}',
                publication_date=f'20{book_id}',
                ISBN=9780547951973,
                page_count=1000,
                cover_src='some/path',
                language='en',
            )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_lists_all_books(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertFalse(len(response.context['object_list']) == 10)
        self.assertTrue(len(response.context['object_list']) == 11)


class ListImportViewTest(TestCase):
    def test_successful_redirect(self):
        response = self.client.get(reverse('list'), {'title': 'Hobbit', 'author': 'Tolkien'})
        self.assertRedirects(response, '/home.html')

    def test_failure_redirect(self):
        response = self.client.get(reverse('list'), {'title': 'asdagsadasd', 'author': 'sdgsdfasdasd'})
        self.assertRedirects(response, '/import.html')


class BookAPIViewTest(TestCase):
    """ Test module for GET all puppies API """

    def setUp(self):
        number_of_books = 6

        for book_id in range(number_of_books):
            Book.objects.create(
                title=f'Title {book_id}',
                author=f'book {book_id}',
                publication_date=f'20{book_id}',
                ISBN=9780547951973,
                page_count=1000,
                cover_src='some/path',
                language='en',
            )

    def test_get_all_books(self):
        # get API response
        response = self.client.get(reverse('api'))
        # get data from db
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        # set uniform data format
        serializer_payload = loads(dumps(serializer.data))
        response_payload = loads(dumps(response.data))

        self.assertEqual(response_payload['results'], serializer_payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
