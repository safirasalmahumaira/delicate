from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render, redirect
from main.forms import ItemForm
from main.models import Item

def show_main(request):
    item_entries = Item.objects.all()
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
        'item_entries': item_entries
    }
    return render(request, 'main.html', context)

def create_item_entry(request):
    form = ItemForm(request.POST or None)
    if form.is_valid() and request.method == "POST":
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
