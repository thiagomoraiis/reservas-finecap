from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from .forms import LoginForm, UserForm

# Create your views here.
def user_logout(request):
    logout(request)
    return redirect('login')

def user_login(request):
    if request.method == 'POST':
        form_login = LoginForm(request.POST)
        
        if form_login.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('login')
    
    else:
        form_login = LoginForm()

    context = {
        'login_data': form_login
    }
    
    return render(request, 'user/form_login.html', context)

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            user = form.save()
            user.is_active = True
            user.is_staff = True
            user.save()

            return redirect('login')
    
    else:
        form = UserForm()
    
    context = {
        'form': form
    }

    return render(request, 'user/form_register.html', context)