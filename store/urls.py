from django.urls import path 
from .views import *
from master.models import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('Pharma/', Pharma, name='Pharma'),
    path('Store/', Store, name='Store'),
    path('upload-medicine/', upload_medicine, name='upload_medicine'),
    path('add_Mediine/', add_medicine, name='add_medicine'),
    path('CartItems/', CartItems, name='CartItems'),
    path('orderitem/', orderitem, name='orderitem'),
    path('orderplace/<int:id>/', orderplace, name='orderplace'),
    path('delMedicine/<int:id>/', delMedicine, name='delMedicine'),
    path('editMedicine/<int:id>/', editMedicine, name='editMedicine'),
    path('update-medicine/<int:id>/', update_medicine, name='update_medicine'),
    path('sales/', sales, name='sales')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)