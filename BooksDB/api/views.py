from rest_framework import viewsets
from .serializers import BookSerializer
from rest_framework import permissions
from BooksDB.models import Book
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView


class BookViewSet(ListAPIView):
    """
    API endpoint that allows books to be viewed or edited.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # to require permissions change below to [permissions.IsAuthenticated]
    permission_classes = (permissions.AllowAny,)
    http_method_names = ['get']


    # def get(self, request, *args, **kwargs):
    #     """
    #     List all the todo items for given requested user
    #     """
    #     books = Book.objects.all()
    #     serializer = BookSerializer(books, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

    def get_queryset(self):
        queryset = Book.objects.all()
        author = self.request.query_params.get('author', None)
        if author is not None:
            queryset = queryset.filter(author=author)
        return queryset

    # def post(self, request, *args, **kwargs):
    #     '''
    #     Create the Todo with given todo data
    #     '''
    #     data = {
    #         'task': request.data.get('task'),
    #         'completed': request.data.get('completed'),
    #         'user': request.user.id
    #     }
    #     serializer = BookSerializer(data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
