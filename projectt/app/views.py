from django.shortcuts import render,redirect
from app.models import Clients
from passlib.hash import pbkdf2_sha512
from django.core.files.storage import FileSystemStorage
from django.conf import settings

# Create your views here.

def index(req):
    if not "done" in req.COOKIES:
        return redirect("/login")
    else:
        return render(req,"index.html")

def login(req):
    if not "done" in req.COOKIES:
        return render(req,"login.html")
    else:
        return redirect("/")

def loginn(req):
    username=req.POST["username"]
    email=req.POST["email"]
    key=req.POST["key"]
    o=Clients.objects.filter(username__icontains=username)
    oo=0
    for i in o:
        oo=pbkdf2_sha512.verify(key,i.keykey)
    print("oo:",oo)
    if oo:
        res=render(req,"loginn.html")
        res.set_cookie("done",1)
        return res
    else:
        return render(req,"login.html")

def logout(req):
    res=render(req,"logout.html")
    res.delete_cookie("done")
    return res

def signup(req):
    if not "done" in req.COOKIES:
        return render(req,"signup.html")
    else:
        return redirect("/")

def signupp(req):
    username=req.POST["username"]
    email=req.POST["email"]
    key=req.POST["key"]
    keyy=pbkdf2_sha512.hash(key,rounds=512000,salt=b"0t1u2v3w4x5y6z")
    if Clients.objects.create(username=username,email=email,keykey=keyy):
        res=render(req,"signupp.html")
        res.set_cookie("done",1)
        return res
    else:
        return render(req,"signup.html")

def cookies(req):
    if "csrftoken" in req.COOKIES:
        cur=1
        res=render(req,"cok.html")
        res.set_cookie("done",cur)
        return res
    else:
        return redirect("/login");

def files(req):
    if not "done" in req.COOKIES:
        return redirect("/login")
    else:
        if req.method=="POST" and req.FILES["f"]:
            mf=req.FILES["f"]
            fs=FileSystemStorage()
            fn=fs.save(mf.name,mf)
            uploaded=fs.url(fn)
            return render(req,"files.html",{"uploaded":uploaded})
        else:
            return render(req,"files.html")

def chat(req):
    if not "done" in req.COOKIES:
        return redirect("/login")
    else:
        return render(req,"chatt.html")
