from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

from .forms import ImageForm
from .data import *

# Create your views here.

def index(request):
    basket.clear()
    return render(request, 'main\index.html', {'products': products, 'categoryes': categoryes, 'category': category, 'basket': basket, 'basketLen': len(basket), 'isAdmin': isAdmin, 'isLogin': isLogin, 'user': user})

def Basket(request):
    if request.method == 'POST':
        print(request.POST)
        sum = 0
        for index in range(int(request.POST['count'])):
            print("!!! " + str(index))

            isFound = False
            if len(basket) > 0:
                for item in basket:
                    if item['product']['name'] == request.POST[str(index)]:
                        isFound = True
                        break

            print(GetProductByName(request.POST[str(index)]))
            
            sum += float(GetProductByName(request.POST[str(index)])['price'])
            if not isFound:
                basket.append({
                    'product': GetProductByName(request.POST[str(index)])
                })
        return render(request, 'main\Basket.html', {'basket': basket, 'SumPrice': float('{:.2f}'.format(sum))})

def SingIn(request):
    if request.method == 'POST':
        luser = request.POST

        for _user in users:
            if _user['login'] == luser['login'] and _user['password'] == luser['password']:
                global isLogin, isAdmin, user
                isLogin = True
                isAdmin = bool(_user['isAdmin'])
                user = _user
                basket.clear()

                print(isAdmin)
                return render(request, 'main\index.html', {'products': products, 'categoryes': categoryes, 'category': category, 'basket': basket, 'basketLen': len(basket), 'isAdmin': isAdmin, 'isLogin': isLogin, 'user': user})
        return render(request, 'main\SingIn.html', {'isFailed': True})
    else: return render(request, 'main\SingIn.html')

def SingUp(request):
    if request.method == 'POST':
        ruser = request.POST
        form = ImageForm(ruser, request.FILES)

        if form.is_valid():
            form.save()
            img_obj = form.instance

            global users, user, isLogin, isAdmin

            for _user in users:
                if _user['login'] == ruser['login']:
                    return render(request, 'main\SingUp.html', {'form': ImageForm})

            users.append({
                'login': ruser['login'],
                'password': ruser['password'],
                'isAdmin': False,
                'img': img_obj.image.url
            })

            isLogin = True
            isAdmin = False
            user = users[len(users) - 1]
            basket.clear()

            return render(request, 'main\index.html', {'products': products, 'basket': basket, 'categoryes': categoryes, 'category': category, 'basketLen': len(basket), 'isAdmin': isAdmin, 'isLogin': isLogin, 'user': user})
    else: return render(request, 'main\SingUp.html', {'form': ImageForm})

def Exit(request):
    global isAdmin, isLogin, user
    isAdmin = False
    isLogin = False
    user = None

    basket.clear()
    return render(request, 'main\index.html', {'products': products, 'categoryes': categoryes, 'category': category, 'basket': basket, 'basketLen': len(basket), 'isAdmin': isAdmin, 'isLogin': isLogin, 'user': user})

def Sort(request):
    global category
    category = None if request.POST['Category'] == "Все" else request.POST['Category']
    basket.clear()
    return render(request, 'main\index.html', {'products': products, 'categoryes': categoryes, 'category': category, 'basket': basket, 'basketLen': len(basket), 'isAdmin': isAdmin, 'isLogin': isLogin, 'user': user})
    
def Search(request):
    resul = []
    basket.clear()
    for item in products:
        if str(item['name']).lower() == request.POST['Search'].lower() or str(item['name']).lower().__contains__(request.POST['Search'].lower()):
            if category != None and item['category'] == category:
                resul.append(item)
            else:
                resul.append(item)

    if len(resul) > 0:
        return render(request, 'main\index.html', {'products': resul, 'categoryes': categoryes, 'category': category, 'basket': basket, 'basketLen': len(basket), 'isAdmin': isAdmin, 'isLogin': isLogin, 'user': user})
    else:
        if category == None:
            return render(request, "main\Error.html", {'error': "По запросу '" + request.POST['Search'] + "' ничего не найдено!"})
        else:
            return render(request, "main\Error.html", {'error': "В категории '" + category + "' по запросу '" + request.POST['Search'] + "' ничего не найдено!"})

def Remove(request):
    name = request.POST['name']

    _list = []

    for item in products:
        if item['name'] != name:
            _list.append(item)

    products.clear()
    for item in _list:
        products.append(item)

    return render(request, 'main\index.html', {'products': products, 'categoryes': categoryes, 'category': category, 'basket': basket, 'basketLen': len(basket), 'isAdmin': isAdmin, 'isLogin': isLogin, 'user': user})

def AddProduct(request):
    if request.method == 'POST':
        newProduct = request.POST

        form = ImageForm(newProduct, request.FILES)

        if form.is_valid():
            form.save()
            img_obj = form.instance

            products.append({
                'name': newProduct['name'],
                'category': newProduct['category'],
                'img': img_obj.image.url,
                'price': float(newProduct['price'])
            })
        return render(request, 'main\index.html', {'products': products, 'categoryes': categoryes, 'category': category, 'basket': basket, 'basketLen': len(basket), 'isAdmin': isAdmin, 'isLogin': isLogin, 'user': user})
    else:
        newCat = []
        for cat in categoryes:
            if cat != "Все": newCat.append(cat)

        return render(request, 'main\AddProduct.html', {'form': ImageForm, 'categoryes': newCat})

def Change(request):
    if request.method == 'POST':
        newProduct = request.POST

        for item in products:
            if item['name'] == newProduct['oldName']:

                item['name'] = newProduct['name']
                item['category'] = newProduct['category']
                item['img'] = newProduct['img']
                item['price'] = float(newProduct['price'])
                break

        return render(request, 'main\index.html', {'products': products, 'categoryes': categoryes, 'category': category, 'basket': basket, 'basketLen': len(basket), 'isAdmin': isAdmin, 'isLogin': isLogin, 'user': user})
    else:
        newCat = []
        for cat in categoryes:
            if cat != "Все": newCat.append(cat)

        for item in products:
            if item['name'] == request.GET['name']:
                return render(request, 'main\Change.html', {'categoryes': newCat, 'product': item})