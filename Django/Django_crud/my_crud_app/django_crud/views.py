# crud/views.py

from django.shortcuts import render, redirect

# Simulated data storage using a Python dictionary
data = {}

def home(request):
    return render(request, 'django_crud/list.html')

def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        data[email] = {'name': name, 'email': email}
        return redirect('list')
    return render(request, 'django_crud/create.html')

def list(request):
    return render(request, 'django_crud/list.html', {'data': data})

def update(request, email):
    user = data.get(email)
    if request.method == 'POST':
        if user:
            new_name = request.POST.get('name')
            new_email=request.POST.get('email')
            user['name'] = new_name
            user['email'] =new_email
            return redirect('list')
        else:
            # Handle case where user doesn't exist
            return redirect('list')
    if user:
        return render(request, 'django_crud/update.html', {'user': user})
    else:
        # Handle case where user doesn't exist
        return redirect('list')


def delete(request, email):
    if email in data:
        del data[email]
    return redirect('list')