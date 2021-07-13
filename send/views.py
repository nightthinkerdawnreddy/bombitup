from django.shortcuts import render
from django.http import HttpResponse
from .seleniumtesting import mainfunction

# Create your views here.
def home(request):
    if request.method == 'POST':
        number=request.POST['phonenumber']
        noofmessages=request.POST['noofmessages']
        mainfunction(number,int(noofmessages))
        return render(request,'thanks.html')
    return render(request,'index.html')