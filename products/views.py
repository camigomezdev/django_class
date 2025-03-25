from django.shortcuts import get_object_or_404, render
from .models import Product


def get_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, "products/detail.html", {"product": product})


def index(request):
    products = Product.objects.order_by("-created_date")[:5]
    context = {"products": products}
    return render(request, "products/index.html", context)
