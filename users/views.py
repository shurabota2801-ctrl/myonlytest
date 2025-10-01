from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('users:login'))
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form, 'title':'Регистрация'})
        