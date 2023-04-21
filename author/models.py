from django.db import models
from .validators import validate_file_extension
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Author(models.Model):
    
    def nameFile(instance, filename):
        return '/'.join(['pdfs', str(instance.title), filename])
    
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    body = models.TextField(max_length=300)
    summary = models.CharField(max_length=60)
    documents = models.FileField(upload_to=nameFile, validators=[validate_file_extension], blank=False)
    categories = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
