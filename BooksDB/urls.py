"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.conf.urls import url
from BooksDB.views import HomePageView, BookUpdateView, BookCreateView, BookImportView, ListImportView, InfoView


urlpatterns = [
    url(r"^$", HomePageView.as_view(), name='home'),
    url("home", HomePageView.as_view(), name='home'),
    url(r"add", BookCreateView.as_view(), name='add'),
    url(r"update/(?P<pk>\d+)/$", BookUpdateView.as_view(), name='update'),
    url("import", BookImportView.as_view(), name='import'),
    url("list", ListImportView.as_view(), name='list'),
    url("info", InfoView.as_view(), name='list'),
    path('api/', include('BooksDB.api.urls')),
]
