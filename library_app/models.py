from django.db import models

# Create your models here.
from django.utils import timezone


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_creating = models.DateField(default=timezone.now, blank=False, null=False)
    date_of_birth = models.DateField(blank=False, null=False)
    keyword = models.CharField(max_length=200)
    book_revenue = models.FloatField(null=True, blank=True)


class Book(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(null=False, blank=False)
    review = models.CharField(max_length=500)
    language = (
        ('UA', 'Ukrainian'),
        ('RU', 'Russian'),
        ('EN', 'English'),
        ('Fr', 'French')
    )
    date_of_publication = models.DateField(null=False, blank=False)
    binding = (
        ('Soft', 'Soft'),
        ('Hard', 'Hard')
    )
    iSBN = (
        ('123', '123'),
        ('456', '456'),
        ('789', '789')
    )
    price = models.FloatField(null=False, blank=False, default=20)


class Sale(models.Model):
    order_number = models.IntegerField(null=False, blank=False)
    books_in_order = models.ManyToManyField('Book', related_name='orders')
    date_of_order = models.DateField(default=timezone.now, blank=False, null=False)
    order_status = (
        ('In_progress', 'In_progress'),
        ('Done', 'Done'),
        ('Canceled', 'Canceled')
    )