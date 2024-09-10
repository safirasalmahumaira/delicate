from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'Name' : 'Safira Salma Humaira',
        'NPM' : '2306245850',
        'Class': 'PBP F',
        'Products': [
            {'Name': 'Moisturizer', 'Price': 250.000, 'Description': 'This lightweight moisturizer is specially formulated for oily skin. It helps to control excess sebum production without drying out your skin. The non-greasy formula provides hydration while maintaining a shine-free finish. Perfect for those seeking a balanced and healthy complexion.'},
            {'name': 'Facial Wash', 'Price': 150.000, 'Description': 'Our facial wash is specially formulated to combat excess oil and shine. It gently cleanses pores, removing impurities and preventing breakouts. With its refreshing formula, your skin will feel clean, mattified, and balanced.'},
            # Add more items as needed
        ],
    }

    return render(request, "main.html", context)
