from django.shortcuts import render, redirect
from Shop.models import Kids, Clothes, Cardio, Gym_equipments
from django.views import View
from User.models import Cart
# Create your views here.


def index(request):
    return render(request, 'core/index.html')


def base(request):
    return render(request, 'core/base.html', {'email': request.session.get('user')})


class Kid(View):
    def get(self, request):
        if request.method == 'GET':
            product = Kids.objects.all()
            return render(request, 'core/kids.html', {'products': product})

    def post(self, request):
        product_name = request.POST['product']
        product = Kids.objects.get(name=product_name)
        cart = Cart.objects.filter(title=product_name)
        v = 1

        if request.session.get('user'):
            if len(cart) == 1:
                Qty = cart[0].quantity + 1
                Cart.objects.update_or_create(
                    title=product.name, defaults={'quantity': Qty})
            else:
                entry = Cart(title=product.name, price=product.price,
                             image=product.image, quantity=v, section='Kids')
                entry.save()
        else:
            cart = request.session.get('cart')

            if cart:
                if product.name in cart.keys():
                    Qty = cart[product.name]['quantity'] + 1
                    request.session['cart'][product.name].update(
                        {'quantity': Qty})
                    request.session.modified = True
                else:
                    cart[product.name+'Kids'] = {'name': product.name,
                                                 'price': product.price, 'description': product.dec, 'quantity': v, 'section': 'Kids', 'image': product.image.url}
            else:
                request.session['cart'] = {}
                cart = request.session.get('cart')
                cart[product.name+'Kids'] = {'name': product.name,
                                             'price': product.price, 'description': product.dec, 'quantity': v, 'section': 'Kids', 'image': product.image.url}
            request.session['cart'] = cart
        return redirect('kid')


class Crdio(View):
    def get(self, request):
        if request.method == 'GET':
            product = Cardio.objects.all()
            return render(request, 'core/cardio.html', {'products': product})

    def post(self, request):
        product_name = request.POST['product']
        product = Cardio.objects.get(name=product_name)
        cart = Cart.objects.filter(title=product_name)
        v = 1

        if request.session.get('user'):
            if len(cart) == 1:
                Qty = cart[0].quantity + 1
                Cart.objects.update_or_create(
                    title=product.name, defaults={'quantity': Qty})
            else:
                entry = Cart(title=product.name, price=product.price,
                             image=product.image, quantity=v, section='Cardio')
                entry.save()
        else:
            cart = request.session.get('cart')

            if cart:
                if product.name in cart.keys():
                    Qty = cart[product.name]['quantity'] + 1
                    request.session['cart'][product.name].update(
                        {'quantity': Qty})
                    request.session.modified = True
                else:
                    cart[product.name+'Cardio'] = {'name': product.name,
                                                   'price': product.price, 'description': product.dec, 'quantity': v, 'section': 'Cardio', 'image': product.image.url}
            else:
                request.session['cart'] = {}
                cart = request.session.get('cart')
                cart[product.name+'Cardio'] = {'name': product.name,
                                               'price': product.price, 'description': product.dec, 'quantity': v, 'section': 'Cardio', 'image': product.image.url}
            request.session['cart'] = cart
        return redirect('cardio')


class Gym_equipment(View):
    def get(self, request):
        if request.method == 'GET':
            product = Gym_equipments.objects.all()
            return render(request, 'core/gym_equipments.html', {'products': product})

    def post(self, request):
        product_name = request.POST['product']
        product = Gym_equipments.objects.get(name=product_name)
        cart = Cart.objects.filter(title=product_name)
        v = 1

        if request.session.get('user'):
            if len(cart) == 1:
                Qty = cart[0].quantity + 1
                Cart.objects.update_or_create(
                    title=product.name, defaults={'quantity': Qty})
            else:
                entry = Cart(title=product.name, price=product.price,
                             image=product.image, quantity=v, section='Gym_equipments')
                entry.save()
        else:
            cart = request.session.get('cart')

            if cart:
                if product.name in cart.keys():
                    Qty = cart[product.name]['quantity'] + 1
                    request.session['cart'][product.name].update(
                        {'quantity': Qty})
                    request.session.modified = True
                else:
                    cart[product.name+'Gym_equipments'] = {'name': product.name,
                                                           'price': product.price, 'description': product.dec, 'quantity': v, 'section': 'Gym_equipments', 'image': product.image.url}
            else:
                request.session['cart'] = {}
                cart = request.session.get('cart')
                cart[product.name+'Gym_equipments'] = {'name': product.name,
                                                       'price': product.price, 'description': product.dec, 'quantity': v, 'section': 'Gym_equipments', 'image': product.image.url}
            request.session['cart'] = cart
        return redirect('gym_equipment')


class Cloth(View):
    def get(self, request):
        if request.method == 'GET':
            product = Clothes.objects.all()
            return render(request, 'core/clothes.html', {'products': product})

    def post(self, request):
        product_name = request.POST['product']
        product = Clothes.objects.get(name=product_name)
        cart = Cart.objects.filter(title=product_name)
        v = 1

        if request.session.get('user'):
            if len(cart) == 1:
                Qty = cart[0].quantity + 1
                Cart.objects.update_or_create(
                    title=product.name, defaults={'quantity': Qty})
            else:
                entry = Cart(title=product.name, price=product.price,
                             image=product.image, quantity=v, section='Clothes')
                entry.save()
        else:
            cart = request.session.get('cart')

            if cart:
                if product.name in cart.keys():
                    Qty = cart[product.name]['quantity'] + 1
                    request.session['cart'][product.name].update(
                        {'quantity': Qty})
                    request.session.modified = True
                else:
                    cart[product.name+'Clothes'] = {'name': product.name,
                                                    'price': product.price, 'description': product.dec, 'quantity': v, 'section': 'Clothes', 'image': product.image.url}
            else:
                request.session['cart'] = {}
                cart = request.session.get('cart')
                cart[product.name+'Clothes'] = {'name': product.name,
                                                'price': product.price, 'description': product.dec, 'quantity': v, 'section': 'Clothes', 'image': product.image.url}
            request.session['cart'] = cart
        return redirect('clothes')


def about(request):
    return render(request, 'core/about.html')


class kidsDetail(View):
    def get(self, request, name):
        if request.method == 'GET':
            product = Kids.objects.filter(name=name)
            return render(request, 'core/detail.html', {'product': product[0], 'pr': Kids})

    def post(self, request, name):
        product = Kids.objects.get(name=name)
        cart = Cart.objects.filter(title=name)
        v = 1
        if len(cart) == 1:
            Qty = cart[0].quantity + 1
            Cart.objects.update_or_create(
                title=product.name, defaults={'quantity': Qty})
        else:
            entry = Cart(title=product.name, price=product.price,
                         image=product.image, quantity=v)
            entry.save()
        return redirect('kidsdetail', name=request.POST['product'])


class gym_equipmentDetail(View):
    def get(self, request, name):
        if request.method == 'GET':
            product = Gym_equipments.objects.filter(name=name)
            return render(request, 'core/detail.html', {'product': product[0], 'pr': Gym_equipments})

    def post(self, request, name):
        product = Gym_equipments.objects.get(name=name)
        cart = Cart.objects.filter(title=name)
        v = 1
        if len(cart) == 1:
            Qty = cart[0].quantity + 1
            Cart.objects.update_or_create(
                title=product.name, defaults={'quantity': Qty})
        else:
            entry = Cart(title=product.name, price=product.price,
                         image=product.image, quantity=v)
            entry.save()
        return redirect('gymeuipmentdetail', name=request.POST['product'])


class cardioDetail(View):
    def get(self, request, name):
        if request.method == 'GET':
            product = Cardio.objects.filter(name=name)
            return render(request, 'core/detail.html', {'product': product[0], 'pr': Cardio})

    def post(self, request, name):
        product = Cardio.objects.get(name=name)
        cart = Cart.objects.filter(title=name)
        v = 1
        if len(cart) == 1:
            Qty = cart[0].quantity + 1
            Cart.objects.update_or_create(
                title=product.name, defaults={'quantity': Qty})
        else:
            entry = Cart(title=product.name, price=product.price,
                         image=product.image, quantity=v)
            entry.save()
        return redirect('cardiodetail', name=request.POST['product'])


class clothesDetail(View):
    def get(self, request, name):
        if request.method == 'GET':
            product = Clothes.objects.filter(name=name)
            return render(request, 'core/detail.html', {'product': product[0], 'pr': Clothes})

    def post(self, request, name):
        product = Clothes.objects.get(name=name)
        cart = Cart.objects.filter(title=name)
        v = 1
        if len(cart) == 1:
            Qty = cart[0].quantity + 1
            Cart.objects.update_or_create(
                title=product.name, defaults={'quantity': Qty})
        else:
            entry = Cart(title=product.name, price=product.price,
                         image=product.image, quantity=v)
            entry.save()
        return redirect('clothesdetail', name=request.POST['product'])
