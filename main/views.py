from django.shortcuts import render

def show_main(request):
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
        ]
    }
    return render(request, 'main.html', context)
