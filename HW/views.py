from django.shortcuts import render
from django.shortcuts import redirect, HttpResponse
from datetime import datetime
from HW.models import Product, Hashtag, Review
from Online_store_HW.forms import ProductCreateForm, ReviewCreateForm
from Online_store_HW.constants import PAGINATION_LIMIT


def hello(request):
    if request.method == "GET":
        return HttpResponse('Hello! Its my project')


def now_date(request):
    if request.method == 'GET':
        return HttpResponse(datetime.now())


def goodbay(request):
    if request.method == 'GET':
        return HttpResponse('Goodby user!')


def main_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        search = request.GET.get('search')
        page = int(request.GET.get('page', 1))

        if search:
            products = products.filter(title__contains=search) | products.filter(description__contains=search)

        max_page = products.__len__() / PAGINATION_LIMIT
        if round(max_page) < max_page:
            max_page = round(max_page) + 1
        else:
            max_page = round(max_page)

        products = products[PAGINATION_LIMIT * (page - 1):PAGINATION_LIMIT * page]

        context = {
            'HW': [
                {
                    'id': product.id,
                    'image': product.image,
                    'title': product.title,
                    'description': product.description,
                    'rate': product.rate,
                    'hashtag': product.hashtags,
                } for product in products
            ],
            'user': request.user,
            'pages': range(1, max_page + 1)
        }
        return render(request, 'product/products.html', context=context)


def hashtags_view(request):
    if request.method == 'GET':
        hashtags = Hashtag.objects.all()

        context = {
            'hashtags': hashtags
        }

        return render(request, 'product/hashtags.html', context=context)


def product_detail_view(request, id):
    if request.method == 'GET':
        product = Product.objects.get(id=id)

        context = {
            'product': product,
            'reviews': product.review.all(),
            'form': ReviewCreateForm
        }

        return render(request, 'product/detail.html', context=context)

    if request.method == 'POST':
        product = Product.objects.get(id=id)
        data = request.POST
        form = ReviewCreateForm(data=data)

        if form.is_valid():
            Review.objects.create(
                text=form.cleaned_data.get('text'),
                product=product
            )

        context = {
            'product': product,
            'review': product.review.all(),
            'form': form
        }

        return render(request, 'product/detail.html', context=context)


def create_product_view(request):
    if request.method == 'GET':
        context = {
            'form': ProductCreateForm
        }

        return render(request, 'product/create.html', context=context)

    if request.method == 'POST':
        data, files = request.POST, request.FILES

        form = ProductCreateForm(data, files)

        if form.is_valid():
            Product.objects.create(
                image=form.cleaned_data.get('image'),
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
                rate=form.cleaned_data.get('rate'),
            )
            return redirect('/HW')

        return render(request, 'product/create.html', context={
            'form': form
        })