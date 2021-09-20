from django.contrib.auth import authenticate, login,logout
from django.shortcuts import redirect, render
# Create your views here.

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username, password)
        user = authenticate(request, username=username,password=password)
        if user is None:
            context = {"error":"Usuario o contraseña inválida"}
            return render(request,"cuentas_usuario/login.html",context)
        login_status= login(request, user)
        print(login_status)
        return redirect('/')
    return render(request,"cuentas_usuario/login.html",{})

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("/")
    return render(request,"cuentas_usuario/logout.html",{})

def register_view(request):
    return render(request,"cuentas_usuario/register.html",{})