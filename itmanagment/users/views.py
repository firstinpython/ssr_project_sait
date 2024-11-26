from django.shortcuts import render

# Create your view here.

def registration(request):
    return render(request,'users/registration.html')

def profile(request):
    return render(request, 'users/profile.html')