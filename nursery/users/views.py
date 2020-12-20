from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import json
from django.contrib.auth import login, authenticate, logout
from users.forms import RegistrationForm,  UserAuthenticationForm
from users.models import (UserData, PlantDetails, OrderDetails)


# Create your views here.

def all_order_view(request):
    data = list(OrderDetails.objects.all().values())
    response_data = {'a': data}

    return JsonResponse(response_data, safe=False)


def all_plant_view(request):
    data = list(PlantDetails.objects.all().values())
    response_data = {'a': data}

    return JsonResponse(response_data, safe=False)


def all_user_view(request):
    data = list(UserData.objects.all().values(
        'first_name', 'username', 'phone'))
    response_data = {'a': data}

    return JsonResponse(response_data, safe=False)


def home_view(request):
    context = {}
    return render(request, 'users/home.html', context)


def registration_view(request):
    context = {}

    if request.POST:
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            name = form.cleaned_data.get('first_name')

            account = authenticate(email=email, password=raw_password)

            login(request, account)
            profile = Userprofile.objects.create(
                user=request.user, username=name, email=email)
            profile.save()

            return redirect('home')

        else:
            context['registration_form'] = form
    else:  # GET
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'users/register.html', context)


def logout_view(request):
    logout(request)
    return redirect('home')


def login_view(request):
    context = {}
    # return redirect("home")

    user = request.user

    if user.is_authenticated:
        return redirect("home")

    if request.POST:
        form = UserAuthenticationForm(request.POST)

        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']

            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect("home")

    else:
        form = UserAuthenticationForm()

    context['login_form'] = form
    return render(request, 'users/login.html', context)
