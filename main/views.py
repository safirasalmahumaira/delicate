from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'Name' : 'Moisturizer',
        'Price': 'Rp250.000',
        'Description': 'This lightweight moisturizer is specially formulated for oily skin. It helps to control excess sebum production without drying out your skin. The non-greasy formula provides hydration while maintaining a shine-free finish. Perfect for those seeking a balanced and healthy complexion.'
    }

    return render(request, "main.html", context)
