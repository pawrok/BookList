from django.conf.urls import url
from django.urls import path, include
from .views import (
    BookViewSet,
)

urlpatterns = [
    path('', BookViewSet.as_view(), name='api')
]