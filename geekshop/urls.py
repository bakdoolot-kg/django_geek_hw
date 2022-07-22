from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from product import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'phone/\d+', views.phone),
    re_path(r'^categories/', views.categories),
    path('', views.homepage),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
