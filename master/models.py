from django.db import models
from app.models import *
# Create your models here.

MEDICINE_TYPE = (
    ('Syrup', 'Syrup'),
    ('Tablet', 'Tablet'),
    ('Vitamin', 'Vitamin'),
)

class Medicine(models.Model):
    name = models.CharField(max_length=25)
    title = models.CharField(max_length=100)
    detail = models.CharField(max_length=250)
    type = models.CharField(max_length=50, choices=MEDICINE_TYPE)
    picture = models.ImageField(upload_to='Medicine')
    amount = models.IntegerField()
    discount_amount = models.IntegerField()


class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE, null=True)
    quantity = models.PositiveIntegerField(default=10)


class profile(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    state = models.CharField(max_length=25)
    zipcode = models.IntegerField()
    phone_no = models.IntegerField()




ORDER_STATUS = (
    ('Accepted', 'Accepted'),
    ('Packed', 'Packed'),
    ('On the Way', 'On the way'),
    ('Delivered','Delivered'),
    ('Cancel', 'Cancel')
)


class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    profile = models.ForeignKey(profile, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    place = models.CharField(max_length=25, choices=ORDER_STATUS, default='Pending')
    quantity = models.PositiveIntegerField(default=10)