from django.shortcuts import render
from django.views import View

# Create your views here.

"""  custom  admin views """

class AdminView(View):

    def get(self,request):
        return render(request,'manager/index.html')