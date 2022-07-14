from django.shortcuts import render, HttpResponse
from .models import Phones


def homepage(request):
    return render(request, "index.html")


def phone(request):
    phone_object = Phones.objects.get(id=1)
    description = f"{phone_object.name}, {phone_object.description}"
    return HttpResponse(description)


def categories(request):
    products = Phones.objects.all()
    data = {"all_phones": products}
    return render(request, "categories.html", context=data)