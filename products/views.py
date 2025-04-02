from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Category
from .forms import CommentsForm


def get_detail(request, product_id):
    product = Product.objects.prefetch_related(
        'comments__user').get(id=product_id)
    comments = product.comments.all()
    form = CommentsForm()
    return render(request, "products/detail.html",
                  {"product": product, "form": form, "comments": comments})


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


@login_required(login_url='login')
def add_new_comment(request, product_id):
    if request.method == 'POST':

        form = CommentsForm(request.POST)

        if form.is_valid():
            user = request.user
            new_comment = form.save(commit=False)
            new_comment.user = user
            new_comment.product = Product.objects.get(id=product_id)

            new_comment.save()

        return redirect('detail', product_id=product_id)

    else:
        return redirect('detail', product_id=product_id)
