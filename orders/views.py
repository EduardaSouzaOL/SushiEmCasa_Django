from django.shortcuts import render

def pagina_orders(request):
    return render(request, 'orders.html')
