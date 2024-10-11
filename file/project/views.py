from django.shortcuts import render,redirect
from .forms import Userform
from .models import User
# Create your views here.
def output (request):
    data=User.objects.all()
    if request.method == "POST":
        am=Userform (request.POST)
        if am.is_valid():
            am.save()
    else:
        am= Userform()
    return render(request, "index.html", {"form":am, "data":data})

def edit(request, id):
    data=User.objects.get(id=id)
    if request.method == "POST":
        am= Userform (request.POST, instance=data)
        if am.is_valid():
            am.save()
            return redirect('/')
    else:
        am= Userform(instance=data)
    return render (request, "edit.html",{"form":am})

def delete(request,id):
    data=User.objects.get(id=id)
    data.delete()
    return redirect('/')
