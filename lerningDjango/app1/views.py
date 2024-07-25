from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from app1.models import Product


# Create your views here.
def index_page(request):
    print(request.user)
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def forkids_page(request):
    print(request.user)
    products = Product.objects.filter(forkids=True)
    return render(request, 'forkids.html', {'products': products})


def discount_page(request):
    print(request.user)
    products = Product.objects.all()
    return render(request, 'withdiscount.html', {'products': products})


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
                             stock=Stock, sale=int(Disc)/100, forkids=ForKids)
        if productadd is not None:
            productadd.save()
            print("yes product")
            return redirect('index')
        else:
            print("no product")
            return redirect('login')
    return render(request, 'index.html')