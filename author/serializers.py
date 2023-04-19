from rest_framework.serializers import ModelSerializer
from .models import Author

class AuthorSerializer(ModelSerializer):


    class Meta:
        model = Author
        fields = ['title', 'body', 'summary', 'documents', 'categories']