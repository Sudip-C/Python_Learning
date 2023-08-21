from django.shortcuts import render, redirect , get_object_or_404
from .models import Dish, Order


def dish_list(request):
    dishes = Dish.objects.all()
    return render(request, 'menu/dish_list.html', {'dishes': dishes})

def add_dish(request):
    if request.method == 'POST':
        dish_name = request.POST['dish_name']
        price = request.POST['price']
        availability = request.POST.get('availability', False) == "True"
        Dish.objects.create(dish_name=dish_name, price=price, availability=availability)
        return redirect('dish_list')
    return render(request, 'menu/add_dish.html')

def update_availability(request, dish_id):
    dish = get_object_or_404(Dish, pk=dish_id)
    if request.method == 'POST':
        new_availability = request.POST.get('availability', False) == "True"
        dish.availability = new_availability
        dish.save()
        

        return redirect('dish_list')
    return render(request, 'menu/update_availability.html', {'dish': dish})

def remove_dish(request, dish_id):
    dish = get_object_or_404(Dish, pk=dish_id)
    if request.method == 'POST':
        dish.delete()
        return redirect('dish_list')
    return render(request, 'menu/remove_dish.html', {'dish': dish})



def take_order(request):
    dishes = Dish.objects.filter(availability=True)
    if request.method == 'POST':
        customer_name = request.POST['customer_name']
        selected_dish_ids = request.POST.getlist('selected_dishes')
        selected_dishes = Dish.objects.filter(pk__in=selected_dish_ids)
        if selected_dishes.count() == len(selected_dish_ids):
            total_price = sum(dish.price for dish in selected_dishes)
            order = Order.objects.create(customer_name=customer_name)
            order.dishes.set(selected_dishes)
            return render(request, 'menu/order_confirmation.html', {'order': order, 'total_price': total_price})
        else:
            error_message = "Please select valid dishes."
            return render(request, 'menu/take_order.html', {'dishes': dishes, 'error_message': error_message})
    return render(request, 'menu/take_order.html', {'dishes': dishes})



def order_list(request):
    status_filter = request.GET.get('status', '')
    if status_filter:
        if status_filter == 'received':
            orders = Order.objects.filter(order_status='received')
        elif status_filter == 'preparing':
            orders = Order.objects.filter(order_status='preparing')
        elif status_filter == 'ready':
            orders = Order.objects.filter(order_status='ready')
        elif status_filter == 'delivered':
            orders = Order.objects.filter(order_status='delivered')
    else:
        orders = Order.objects.all()
    return render(request, 'menu/order_list.html', {'orders': orders, 'status_filter': status_filter})



def update_order_status(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    if request.method == 'POST':
        new_status = request.POST['new_status']
        if new_status in [status[0] for status in order.STATUS_CHOICES]:
            order.order_status = new_status
            order.save()
            return redirect('order_list')
        else:
            error_message = "Invalid status update."
            return render(request, 'menu/update_order_status.html', {'order': order, 'error_message': error_message})
    return render(request, 'menu/update_order_status.html', {'order': order})

