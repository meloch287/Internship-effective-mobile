from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Order
from .forms import OrderForm
from .models import MenuItem

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'orders/order_list.html', {'orders': orders})

def order_create(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Заказ успешно добавлен")
            return redirect('order_list')
    else:
        form = OrderForm()
    return render(request, 'orders/order_form.html', {'form': form})


def order_delete(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        order.delete()
        messages.success(request, "Заказ удалён")
        return redirect('order_list')
    return render(request, 'orders/order_confirm_delete.html', {'order': order})

def order_update_status(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        new_status = request.POST.get('status')
        if new_status in dict(Order.STATUS_CHOICES):
            order.status = new_status
            order.save()
            messages.success(request, "Статус заказа обновлён")
            return redirect('order_list')
        else:
            messages.error(request, "Неверный статус")
    return render(request, 'orders/order_update_status.html', {
        'order': order,
        'status_choices': Order.STATUS_CHOICES
    })

def menu_list_api(request):
    menu_items = MenuItem.objects.all()
    data = [
        {
            "id": item.id,
            "name": item.name,
            "price": float(item.price),
            "category": item.get_category_display(),
            "description": item.description,
        }
        for item in menu_items
    ]
    return JsonResponse(data, safe=False)
