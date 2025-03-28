from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from .models import Product, Category


def get_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, "products/detail.html", {"product": product})


def index(request):
    products = Product.objects.select_related(
        'category').order_by("-created_date")

    context = {"products": products}
    return render(request, "products/index.html", context)


@login_required(login_url='login')
def get_products_by_category(request, category_id):
    category = Category.objects.get(id=category_id)
    products = category.products.all()
    context = {"category": category, "products": products}
    return render(request, "products/index.html", context)
