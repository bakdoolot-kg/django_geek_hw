from django.contrib import admin
from django.urls import path
from product import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage),
    path('phone/', views.phone)
]
