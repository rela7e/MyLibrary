# Generated by Django 5.0.6 on 2024-05-21 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_book_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='published',
            field=models.IntegerField(null=True),
        ),
    ]