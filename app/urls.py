from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('login/', views.loginuser, name='login'),
    path('logout/', views.logoutuser, name='logout'),
    path('registration/', views.customerregistration, name='customerregistration'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
