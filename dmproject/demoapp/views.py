from django.http import HttpResponse
from django.shortcuts import render
from . models import Place, People

# Create your views here.
# def operations(request):
#     x = int(request.GET['fnum'])
#     y = int(request.GET['snum'])
#     a = x + y
#     s = x - y
#     m = x * y
#     d = x / y
#     return render(request, "contact.html", {'add':a,'sub':s,'mul':m, 'div':d})

def demo(request):
    obj = Place.objects.all()
    obj2 = People.objects.all()
    return render(request, "index.html", {'result':obj, 'people':obj2})
