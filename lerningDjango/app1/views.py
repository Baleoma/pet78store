from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from app1.models import Product, Cart


# Create your views here.
def index_page(request):
    print(request.user)
    products = Product.objects.all()
    cart = Cart.objects.all()
    return render(request, 'index.html', {'products': products, 'cart': cart})


def forkids_page(request):
    print(request.user)
    products = Product.objects.filter(forkids=True)
    cart = Cart.objects.all()
    return render(request, 'forkids.html', {'products': products, 'cart': cart})


def discount_page(request):
    print(request.user)
    products = Product.objects.all()
    cart = Cart.objects.all()
    return render(request, 'withdiscount.html', {'products': products, 'cart': cart})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print("yes user")
            return redirect('index')
        else:
            print("no user")
            return redirect('index')
    return render(request, 'index.html')


def user_logout(request):
    logout(request)
    return redirect('index')


def user_reg(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username=username, password=password)
        user.save()
        if user is not None:
            login(request, user)
            print("yes user")
            return redirect('index')
    return render(request, 'index.html')


def product(request):
    if request.method == 'POST':
        Image = request.FILES.get('Image')
        Name = request.POST.get('Name')
        Desk = request.POST.get('Desk')
        Price = request.POST.get('Price')
        Stock = request.POST.get('Stock')
        ForKids = request.POST.get('ForKids', False)
        Disc = request.POST.get('Disc')

        # Проверка чекбокса
        if ForKids == 'on':
            ForKids = True
        else:
            ForKids = False

        productadd = Product(image=Image, name=Name, description=Desk, price=Price,
                             stock=Stock, sale=int(Disc) / 100, forkids=ForKids)
        if productadd is not None:
            productadd.save()
            print("yes product")
            return redirect('index')
        else:
            print("no product")
            return redirect('login')
    return render(request, 'index.html')


def addToCart(request):
    if request.method == 'POST':
        user_id = request.user.id
        product_id = request.POST.get('product_id')
        if user_id and product_id:
            toCart = Cart(user_id=user_id, product_id=product_id)
            toCart.save()
            print(toCart)
            return redirect('index')
    return redirect('index')

