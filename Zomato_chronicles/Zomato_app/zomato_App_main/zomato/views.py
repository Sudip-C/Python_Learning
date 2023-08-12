import json
from django.shortcuts import render,redirect
from django.http import HttpResponse

orders=[]

def home(request):
    return render(request, "zomato/home.html")


def menu(request):
    # Read menu data from the JSON file
    with open("zomato/menu_data.json") as file:
        menu_data = json.load(file)
    
    context = {
        "menu": menu_data
    }
   
    return render(request, "zomato/menu.html", context)



def add_dish(request):
    if request.method == 'POST':
        # Read existing menu data from the JSON file
        with open("zomato/menu_data.json") as file:
            menu_data = json.load(file)
        
        # Get the data from the form
        new_dish = {
            "id": len(menu_data) + 1,  # Generate a new ID
            "name": request.POST.get('name'),
            "price": float(request.POST.get('price')),
            "availability": request.POST.get('availability') == 'on'  # Convert checkbox value to boolean
        }
        
        # Add the new dish to the menu
        menu_data.append(new_dish)
        
        # Write the updated menu data back to the JSON file
        with open("zomato/menu_data.json", "w") as file:
            json.dump(menu_data, file, indent=4)
        
        return redirect('menu')  # Redirect to the menu page

    return render(request, "zomato/add_dish.html")

def remove_dish(request,dish_id):
    # Read existing menu data from the JSON file
    with open("zomato/menu_data.json") as file:
        menu_data = json.load(file)
    
    # Find the dish to remove
    for dish in menu_data:
        if dish['id'] == int(dish_id):
            menu_data.remove(dish)
            break
    
    # Write the updated menu data back to the JSON file
    with open("zomato/menu_data.json", "w") as file:
        json.dump(menu_data, file, indent=4)
    
    return redirect('menu')  # Redirect to the menu page

def update_availability(request, dish_id):
    # Read existing menu data from the JSON file
    with open("zomato/menu_data.json") as file:
        menu_data = json.load(file)
    
    # Find the dish to update
    for dish in menu_data:
        if dish['id'] == int(dish_id):
            dish['availability'] = not dish['availability']
            break
    
    # Write the updated menu data back to the JSON file
    with open("zomato/menu_data.json", "w") as file:
        json.dump(menu_data, file, indent=4)
    
    return redirect('menu')  # Redirect to the menu page



def take_order(request):
    if request.method == 'POST':
        # Read existing menu data from the JSON file
        with open("zomato/menu_data.json") as file:
            menu_data = json.load(file)
        
        
        customer_name = request.POST.get('customer_name')
        dish_ids = request.POST.getlist('dish_ids')
        
        # Check if each dish is available
        available_dishes = [dish for dish in menu_data if dish['id'] in map(int, dish_ids) and dish['availability']]
        
        if len(available_dishes) == len(dish_ids):
           
            order_id = len(orders) + 1
            
            # Example: Set the initial order status as 'received'
            order_status = 'received'
            
            # Example: Store the order data
            order_data = {
                'order_id': order_id,
                'customer_name': customer_name,
                'dish_ids': dish_ids,
                'status': order_status,
            }
            orders.append(order_data)  # You need to define the "orders" list at the beginning of your views.py
            
            return redirect('orders')  # Redirect to the orders page
        else:
            # Some selected dishes are not available
            error_message = "Some of the selected dishes are not available. Please review your order."
            context = {
                'menu': menu_data,
                'error_message': error_message,
            }
            return render(request, "zomato/take_order.html", context)

    # If the request method is not POST, display the form
    with open("zomato/menu_data.json") as file:
        menu_data = json.load(file)
    context = {
        'menu': menu_data,
        'error_message': None,
        
    }
    return render(request, "zomato/take_order.html", context)



def my_orders(request):
    with open("zomato/menu_data.json") as file:
        menu_data = json.load(file)

    total_sale = calculate_total_sale(orders, menu_data)

    context = {
        'orders': orders,
        'total_sale': total_sale,
    }
    return render(request, "zomato/orders.html", context)

def calculate_total_sale(orders, menu_data):
    try:
        total_sale = 0
        for order in orders:
            for dish_id in order['dish_ids']:
                dish = next((item for item in menu_data if item['id'] == dish_id), None)
                if dish:
                    total_sale += dish['price']
        return total_sale
    except (TypeError, KeyError) as e:
        return 0
    

def update_order_status(request, order_id, new_status):
    order_to_update = next((order for order in orders if order['order_id'] == order_id), None)
    
    if order_to_update:
        # Update the status of the order
        order_to_update['status'] = new_status
        # Redirect to the orders page to view the updated list of orders
        return redirect('orders')
    else:
        # Order with the specified ID not found
        error_message = "Order not found. Please check the order ID."
        context = {
            'orders': orders,
            'error_message': error_message,
        }
        # Render the orders page with the error message
        return render(request, "zomato/orders.html", context)

