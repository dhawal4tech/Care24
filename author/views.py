from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Author
from .serializers import AuthorSerializer
from rest_framework import permissions, filters
from django_filters.rest_framework import DjangoFilterBackend



class AuthorList(ListCreateAPIView):

    serializer_class = AuthorSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = [filters.SearchFilter]

    search_fields = ['id', 'title', 'body', 'summary', 'documents']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
    def get_queryset(self):
        return Author.objects.filter(owner=self.request.user)
    

class AuthorDetailView(RetrieveUpdateDestroyAPIView):

    serializer_class = AuthorSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field="id"
    
    def get_queryset(self):
        return Author.objects.filter(owner=self.request.user)
