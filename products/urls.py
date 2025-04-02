from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:product_id>/detail", views.get_detail, name="detail"),
    path("<int:product_id>/add-comment",
         views.add_new_comment, name="add_new_comment"),
    path("category/<int:category_id>",
         views.get_products_by_category, name="category"),
]
