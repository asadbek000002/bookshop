from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def register(request, ):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('login')
    context = {
        'form': form
    }
    return render(request, 'registration/signup.html', context)