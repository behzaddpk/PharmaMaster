from django.shortcuts import render, redirect
from master.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def Pharma(request):
    medicine = Medicine.objects.all()
    order = Order.objects.all()


    context = {
        'medicine':medicine,
        'order':order
    }
    return render(request, 'Pharma.html', context)


@login_required
def Store(request):
    medicine = Medicine.objects.all()


    context = {
        'medicine': medicine
    }
    return render(request, 'store.html', context)



@login_required
def upload_medicine(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        title = request.POST.get('title')
        detail = request.POST.get('detail')
        type = request.POST.get('type')
        picture = request.FILES.get('product_img')
        amount = request.POST.get('actualamount')
        discount_amount = request.POST.get('discountamount')

        medicine = Medicine(
            name=name,
            title=title,
            detail=detail,
            type=type,
            picture=picture,
            amount=amount,
            discount_amount=discount_amount
        )
        medicine.save()
        messages.success(request, 'Medicine Uploaded')
        return redirect('Store')
    else:
        messages.alert(request, 'data not stored')
        return redirect('Store')

@login_required
def add_medicine(request):
    return render(request, 'add_medicine.html')

@login_required
def CartItems(request):
    cart = Cart.objects.all()


    context = {
        'cartitem': cart
    }
    return render(request, 'CartItems.html', context)

@login_required
def orderitem(request):
    order = Order.objects.all()


    context = {
        'order':order
    }
    return render(request, 'orderitem.html', context)

@login_required
def orderplace(request, id):
    order = Order.objects.get(id=id)
    
    if request.method == 'POST':
        place = request.POST.get('place')
        order.place = place
        order.save()
        messages.success(request, 'Order status updated successfully.')


    context = {
        'order': order
    }
    return render(request, 'orderplace.html', context)

@login_required
def editMedicine(request, id):
    medicine = Medicine.objects.get(id=id)


    context = {
        'medicine': medicine
    }
    return render(request, 'editMedicine.html', context)

@login_required
def update_medicine(request, id):
    medicine = Medicine.objects.get(id=id)

    medicine.name = request.POST.get('name')
    medicine.title = request.POST.get('title')
    medicine.detail = request.POST.get('detail')
    medicine.type = request.POST.get('type')
    if request.FILES.get('picture'):
            medicine.picture = request.FILES['picture']
    medicine.amount = request.POST.get('actualamount')
    medicine.discount_amount = request.POST.get('discountamount')


    medicine.save()
    return redirect('Store')
    
@login_required
def delMedicine(request, id):
    medicine = Medicine.objects.get(id=id)
    medicine.delete()
    return redirect('Store')


@login_required
def sales(request):
    return render(request, 'sales.html')