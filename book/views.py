from cgitb import html
import email
from pydoc import pager
from sre_constants import SUCCESS
from django.shortcuts import redirect, render
from book.models import *
from django.contrib.auth import authenticate, login
from django.contrib import messages

from book.models import asignup

def index(request):
    return render (request, "book/index.html")

def home(request):
    if request.method == "POST":
        uemail = request.POST.get("email")
        upassword = request.POST.get("password")
        data = authenticate(request, email = uemail, password = upassword)
        if data is not None:
            home(request, data)
            return redirect("/library/list")
        else:
            messages.info(request, 'Mail and Password incorrect')
    return render (request, "book/home.html")


def signin(request):
    return render(request, "book/list.html")
    
def signup(request):
    if request.method == "POST":
        uname = request.POST.get("name")
        uemail = request.POST.get("email")
        upassword = request.POST.get("password") 

        obj = asignup( name = uname, email = uemail, password = upassword)

        obj.save()

        return redirect("/library/home/")
    return render (request, "book/signup.html")

def list(request):

    data = book.objects.all()

    return render (request, "book/list.html",{'data':data})
    

def aupdate(request):
    return render (request, "book/aupdate.html")

def abook(request):
    if request.method == "POST":
        bname = request.POST.get("bname")
        writer = request.POST.get("writer")
        quantity = request.POST.get("quantity")

        obj = book( bname = bname, writer = writer, quantity = quantity)
        
        obj.save()

        return redirect("/library/list/")
    return render(request, "book/addbook.html")

def detail(request, id):
    obj = book.objects.get(pk = id)
    return render (request, "book/detail.html",{'obj':obj})

def bupdate(request, id):
    obj = book.objects.get(pk = id)
    if request.method == "POST":
        obj.bname = request.POST.get("bname")
        obj.write = request.POST.get("writer")
        obj.quantity = request.POST.get("quantity")
        obj.save()
        return redirect(f"/library/detail/{obj.id}/")
    return render (request, "book/bupdate.html",{'obj':obj})

def delete(request, id):
    obj = book.objects.get(pk = id)
    obj.delete()
    return redirect("/library/list/")