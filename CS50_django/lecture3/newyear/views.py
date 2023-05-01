from django.shortcuts import render
import datetime
# Create your views here.

def wish(request):
    now = datetime.datetime.now() #date time module
    return render(request, 'newyear/home.html',{
        "newyear":now.month == 1 and now.day == 1}) 
    #last argument in return is dic, that act as variable in templates
