from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:product_id>/detail", views.get_detail, name="detail"),
    path("category/<int:category_id>",
         views.get_products_by_category, name="category"),
]
