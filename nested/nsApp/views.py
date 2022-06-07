from django.shortcuts import render
from rest_framework import generics
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer
from rest_framework.pagination import PageNumberPagination

# for filtering data make sure to install app.
from django_filters.rest_framework import DjangoFilterBackend

# for search filter
from rest_framework import filters

class CustomeClass(PageNumberPagination):
    PAGE_SIZE = 2

class AuthorListView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    pagination_class = CustomeClass
    # new property.

class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # based on which feild you want to filter.
    # column names.
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['title', 'rating', 'author']

    # above code for filtering.
    # now search operations and filter both.
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['title', 'rating', 'author']
    search_fields = ['title', 'rating']
    ordering_fields = ['title', 'rating'] 
    ordering = ['-id'] # default ordering.
    """
        '=title' likewise inside search field.
        ^ for starts with search
        = for exact match search
        @ full text search
        $ Regex search
    """

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

