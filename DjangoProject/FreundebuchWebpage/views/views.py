from django.shortcuts import render, redirect
from Entries.models import CreateCode

def index(request):
    return render(request, "main/main.html")

def dedication(request):
    return render(request, "main/dedication.html")

def enter_creation_code(request):
    match request.method:
        case "GET":
            return render(request, "entries/enter_creation_code.html")
        case "POST":
            code = request.POST.get("code")
            code_objects = CreateCode.objects.filter(secret=code).first()
            if code_objects:
                request.session["code"] = code
                return redirect("/explorer/create/")
            else:
                context = {"failure" : True}
                return render(request, "entries/enter_creation_code.html", context)
        case _:
            context = {"failure": True}
            return render(request, "entries/enter_creation_code.html", context)