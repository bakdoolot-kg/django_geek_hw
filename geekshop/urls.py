from django.contrib import admin
from django.urls import path
from product import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('phone/', views.phone),
    path('categories/', views.categories),
    path('', views.homepage),
]
