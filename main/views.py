from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render, redirect
from main.forms import ItemForm
from main.models import Item
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

@login_required(login_url='/login')
def show_main(request):
    item_entries = Item.objects.filter(user=request.user)
    context = {
        'name': 'Safira Salma Humaira',  # Key is 'name'
        'class': 'PBP F',                # Key is 'class'
        'NPM': '2306245850',
        'products': [
            {
                'Name': 'Moisturizer',
                'Price': '250.000',
                'Description': 'This lightweight moisturizer is specially formulated for oily skin. It helps to control excess sebum production without drying out your skin. The non-greasy formula provides hydration while maintaining a shine-free finish. Perfect for those seeking a balanced and healthy complexion.'
            },
            {
                'Name': 'Facial Wash',
                'Price': '150.000',
                'Description': 'Our facial wash is specially formulated to combat excess oil and shine. It gently cleanses pores, removing impurities while preserving the skin’s natural moisture barrier.'
            }
        ],
        'item_entries': item_entries,
        'last_login': request.COOKIES['last_login'],
    }
    return render(request, 'main.html', context)

def create_item_entry(request):
    form = ItemForm(request.POST or None)
    if form.is_valid() and request.method == "POST":
        item_entry = form.save(commit=False)
        item_entry.user = request.user
        form.save()
        return redirect('main:show_main')
    context = {'form': form}
    return render(request, "create_item_entry.html", context)

def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, item_id):
    data = Item.objects.filter(pk=item_id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, item_id):
    data = Item.objects.filter(pk=item_id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response