from django.shortcuts import render, redirect
from .models import UserData, Cart
from django.contrib import messages
from django.views import View
# Create your views here.


class cart(View):
    def get(self, request):
        if request.session.get('user'):
            w_cart = Cart.objects.all()  # Cart after login
            s=[(i.price*i.quantity) for i in Cart.objects.all()]
            return render(request, 'User/cart.html', {'w_cart': w_cart, 'total':s})
        else:
            try:
                wo_cart = [j for i, j in request.session.get(
                    'cart').items()]  # Cart without login
                print(request.session['cart'])

                return render(request, 'User/cart.html', {'wo_cart': wo_cart})
            except:
                return render(request, 'User/cart.html', {'wo_cart': None, 's':0, 'd':0})

    def post(self, request):
        product = request.POST['product']
        request.session.get('cart').pop(product)
        request.session['cart'] = request.session.get('cart')
        return redirect('cart')


def checkout(request):
    if request.session.get('user'):
        return render(request, 'User/checkout.html')
    return render(request, 'User/login.html')


def login(request):

    if(request.method == 'POST'):

        email = request.POST['email']
        password = request.POST['password']
        checkdata = UserData.objects.filter(
            email=email)

        if (checkdata.exists()):

            if (checkdata[0].email == email and checkdata[0].password == password):
                request.session['user'] = checkdata[0].id
                return render(request, 'core/index.html', {'email': email})
            else:
                message = messages.success(request, "Invalid Credentials!")
                return render(request, 'User/login.html', {'message': message})
        else:
            message = messages.success(request, "Invalid Credentials!")
            return render(request, 'User/login.html', {'message': message})

    return render(request, 'User/login.html')


def register(request):
    if(request.method == 'POST'):

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        phn_nm = request.POST['phn_no']
        checkdata = UserData.objects.filter(
            email=email)

        if (checkdata.exists()):
            if(checkdata != None):
                message = messages.success(request, "Account already exists!")
                return render(request, 'User/register.html', {'message': message})

            else:
                message = messages.success(
                    request, username + " you registered successfully")
                entry = UserData(username=username,
                                 email=email, password=password, phn_no=phn_nm)
                entry.save()
                return render(request, 'User/login.html', {'message': message})
        else:
            message = messages.success(
                request, "Hey " + username + " you registered successfully")
            entry = UserData(username=username,
                             email=email, password=password, phn_no=phn_nm)
            entry.save()
            return render(request, 'User/login.html', {'message': message})

    return render(request, 'User/register.html')


def logout(request):
    try:
        del request.session['user']
    except KeyError:
        pass
    return render(request, 'core/index.html')
