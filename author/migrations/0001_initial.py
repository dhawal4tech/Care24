# Generated by Django 4.1.7 on 2023-04-19 16:07

import author.validators
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('body', models.TextField(max_length=300)),
                ('summary', models.CharField(max_length=60)),
                ('documents', models.FileField(upload_to='doc/', validators=[author.validators.validate_file_extension])),
                ('categories', models.CharField(blank=True, max_length=20, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]