from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from . models import Conversion, History
from .form import CurrencyForm
import requests, json



class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def conversion(request):
    form = CurrencyForm(request.POST)
    url = "http://api.fixer.io/latest?base=AUD"
    response = requests.get(url)
    data = response.json()
    temp = data["rates"]

    if request.user.is_authenticated:
        history = History.objects.filter(user_name=request.user)
    else:
        history = ""

    if form.is_valid():
        from_curr = form.cleaned_data['from_currency']
        val = form.cleaned_data['value']
        to_curr = form.cleaned_data['to_currency']
        base_value = 1/temp[from_curr]
        converted_value = val*base_value*temp[to_curr]
        outputString = str(val) + " " + from_curr + "  =  " + str(round(converted_value, 2)) + " " + to_curr
        historyString = "Converted " + str(val) + " " + from_curr + " to " + to_curr + " on " + data['date']
        h_temp = History(user_name=request.user, history=historyString)
        h_temp.save()
        return render(request, "home.html", {'form':form, 'converted_value':outputString, 'history':history})


    return render(request, "home.html", {'form':form, 'history':history})
