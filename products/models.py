from django.db import models
from django.utils import timezone

from django.core.validators import MinLengthValidator


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sku = models.CharField(max_length=10,
                           validators=[MinLengthValidator(10)])

    category = models.ForeignKey(
        'products.Category', on_delete=models.CASCADE,
        related_name='products', null=True
    )

    discount = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)

    image = models.ImageField(upload_to='media/fotos', null=True, blank=True)
    description = models.TextField()

    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return f'{self.sku} | {self.name}'


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    discount = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)

    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'
