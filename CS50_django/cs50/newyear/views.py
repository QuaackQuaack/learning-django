from django.shortcuts import render
from django.views import View


import datetime

# Create your views here.

class NewYearView(View):
    def get(self, request):
        today  = datetime.datetime.now()
        is_new_year = today.month == 1 and today.day == 1

        context = {
                "is_new_year":is_new_year
                }
        return render(request,"../templates/index.html", context)

        

