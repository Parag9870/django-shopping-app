from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.


def index(request):
    user = "pouya"
    products_numb = 7
    products = Product.objects.all().order_by('id')[:4]
    return render(request, "products/home.html",{
        "name":user,
        "product_numb": products_numb,
        "products": products,
    })

def signup(request):
    return render(request, "products/signup.html")

def product_cat(request, product):
    if product =="suits" or product=="dresses" or product=="shirts" or product=="shoes":
        return HttpResponse(f"Here is the list of our {product}.")
    else:
        return HttpResponse("The page you are looking for doesn't exist.")