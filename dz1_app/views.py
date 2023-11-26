from datetime import timedelta, datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone

from dz1_app.forms import ProductEditForm
from dz1_app.models import Order, Client, Product


def main(request):
    html_main = """
           <!DOCTYPE html>
           <html>
           <head>
               <title>Главная</title>
           </head>
           <body>
               <h1>Добро пожаловать, Пользователь!</h1>              
           </body>
           </html>
       """

    return HttpResponse(html_main)


def about(request):
    html_about = """
               <!DOCTYPE html>
               <html>
               <head>
                   <title>Наверху!</title>
               </head>
               <body>
                   <h1>Обо мне!</h1>
                   <p>Инфа тут</p>
                   tyt!!!    
                   jhhhh!!!          
               </body>
               </html>
           """
    return HttpResponse(html_about)


def all_order(request, client_id: int):
    orders = Order.objects.filter(client_id=client_id)
    context = {
        'orders': orders,
        # 'products': products,
    }
    print(orders)

    return render(request, "dz1_app/all_order.html", context=context)


def client_products(request, client_id):
    end_date = datetime.now().date()
    start_date_7_days_ago = end_date - timedelta(days=7)
    start_date_30_days_ago = end_date - timedelta(days=30)
    start_date_365_days_ago = end_date - timedelta(days=365)

    products_last_7_days = get_client_products_in_date_range(client_id, start_date_7_days_ago, end_date)
    products_last_30_days = get_client_products_in_date_range(client_id, start_date_30_days_ago, start_date_7_days_ago)
    products_last_365_days = get_client_products_in_date_range(client_id, start_date_365_days_ago, start_date_30_days_ago)

    client = Client.objects.get(id=client_id)

    context = {

        'client': client,
        'products_last_7_days': products_last_7_days,
        'products_last_30_days': products_last_30_days,
        'products_last_365_days': products_last_365_days,
    }

    return render(request, 'dz1_app/client_products.html', context)

def get_client_products_in_date_range(client_id, start_date, end_date):
    orders = Order.objects.filter(client__id=client_id, order_date__range=[start_date, end_date])
    print(orders)
    print(start_date, end_date)
    products_with_dates = []
    for order in orders:
        print(order)
        for product in order.products.all():
            print (product)
            products_with_dates.append((product, order.order_date))
            print(products_with_dates)
            print('-----------------')

    return products_with_dates

def get_product(request, product_id: int):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductEditForm(request.POST)
        if form.is_valid():
            product = Product(**form.cleaned_data)
            product.save()
            # return redirect(to=f'get_product/{product_id}')
    else:
        form = ProductEditForm()

    context = {
        'product': product,
        'form': form,
    }
    print(product.name)

    return render(request, "dz1_app/info_product.html", context=context)

