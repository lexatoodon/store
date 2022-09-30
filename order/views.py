from itertools import product
from django.shortcuts import render
from order.forms import OrderForm
from cart.cart import Cart
from order.models import OrderItem
from order.tasks import order_created

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated:
                user = request.user
            else:
                user = None
            form.instance.user = user
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order = order,
                    book = item['book'],
                    price = item['price'],
                    quantity = item['quantity'])
            cart.clear()
            order_created.delay(order.id)
        return render(request, 'order/created.html', {'order': order})
    else:
        form = OrderForm()
    return render(request, 'order/create.html', {'form': form, 'cart': cart})