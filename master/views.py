from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    medicine = Medicine.objects.all()

    context = {
        'medicine': medicine
    }
    return render(request, 'index.html', context)


def medicinedetail(request, id):
    medicine = Medicine.objects.get(id=id)

    context = {
        'medicine': medicine
    }
    return render(request, 'detail.html', context)


def shop(request):
    medicine = Medicine.objects.all()

    context = {
        'medicine': medicine
    }
    return render(request, 'shop.html', context)


@login_required
def add_to_cart(request):
    user = request.user   
    medicine_id = request.GET.get('medicine')
    quantity = request.GET.get('quantity')

    medicine = Medicine.objects.get(id=medicine_id)
    cart = Cart(
        user=user,
        medicine=medicine,
        quantity=quantity
    )
    cart.save()
    

    return redirect('cart')

@login_required
def cart(request):
    user = request.user
    cart_items = Cart.objects.filter(user=user)
    
    # Create a list to store individual total prices
    item_total_prices = []

    # Initialize overall total price
    total_price = 0
    individual_total_price = 0
    # Iterate through cart items and calculate the baseamount and individual total price
    for cart_item in cart_items:
        if cart_item.medicine:
            # Set baseamount
            cart_item.baseamount = cart_item.medicine.amount

            # Calculate individual total price
            individual_total_price = cart_item.quantity * cart_item.baseamount

            # Append the individual total price to the list
            item_total_prices.append(individual_total_price)

            total_price += individual_total_price  # Update the overall total price
        else:
            cart_item.baseamount = 0

    deliveryprice = 50.00
    price = total_price + deliveryprice
    subtotal = total_price  # Subtotal is equal to the total price in this case

    context = {
        'carts': cart_items,
        'item_total_prices': item_total_prices,
        'subtotal': subtotal,
        'total_price': total_price,
        'deliveryprice': deliveryprice,
        'individual_total_price': individual_total_price,
        'price': price
    }
    return render(request, 'cart.html', context)

@login_required
def delusercart(request, id):
    user = request.user
    cart = Cart.objects.filter(user=user, id=id)
    cart.delete()
    return redirect('cart')

@login_required
def checkout(request):
    user = request.user
    cart_items = Cart.objects.filter(user=user)
    Profile = profile.objects.filter(user=user)
    
    # Create a list to store individual total prices
    item_total_prices = []

    # Initialize overall total price
    total_price = 0
    individual_total_price = 0
    # Iterate through cart items and calculate the baseamount and individual total price
    for cart_item in cart_items:
        if cart_item.medicine:
            # Set baseamount
            cart_item.baseamount = cart_item.medicine.amount

            # Calculate individual total price
            individual_total_price = cart_item.quantity * cart_item.baseamount

            # Append the individual total price to the list
            item_total_prices.append(individual_total_price)

            total_price += individual_total_price  # Update the overall total price
        else:
            cart_item.baseamount = 0

    deliveryprice = 50.00
    price = total_price + deliveryprice
    subtotal = total_price  # Subtotal is equal to the total price in this case

    context = {
        'carts': cart_items,
        'item_total_prices': item_total_prices,
        'subtotal': subtotal,
        'total_price': total_price,
        'deliveryprice': deliveryprice,
        'individual_total_price': individual_total_price,
        'price': price,
        'Profile': Profile
    }
    return render(request, 'checkout.html', context)


@login_required
def Profile(request):
    user = request.user
    if request.method == 'POST':
        f_name = request.POST.get('f_name')
        l_name = request.POST.get('l_name')
        address = request.POST.get('address')
        state = request.POST.get('state')
        zipcode = request.POST.get('zipcode')
        phone_no = request.POST.get('phone_no')

        Profile = profile(
            user = user,
            f_name = f_name,
            l_name = l_name,
            address = address,
            state = state,
            zipcode = zipcode,
            phone_no = phone_no
        )
        Profile.save()
        messages.success(request, 'Profile has been Added')

    return redirect('checkout')


@login_required
def ordercomplete(request):
    user = request.user
    profile_id = request.GET.get('profile')
    Profile = profile.objects.get(id=profile_id)
    cart = Cart.objects.filter(user=user)


    for crt in cart:
        order = Order(
            user=user,
            medicine=crt.medicine,
            profile=Profile,
            quantity = crt.quantity
        )
        order.save()
        crt.delete()
        messages.success(request, 'You order was successfuly completed.')
    
    return redirect('ordered')


@login_required
def ordered(request):
    user = request.user
    order = Order.objects.filter(user=user)

    context = {
        'order':order
    }
    return render(request, 'ordered.html', context)


def about(request):
    return render(request, 'about.html')