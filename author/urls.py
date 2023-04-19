from django.urls import path
from .views import AuthorList, AuthorDetailView

urlpatterns = [
    path('', AuthorList.as_view()),
    path('<int:id>', AuthorDetailView.as_view()),
]