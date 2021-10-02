from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect, render
# Create your views here.

def register_view(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user_obj = form.save()
        return redirect("/login")
    context= {"form": form}
    return render(request, "cuentas_usuario/register.html", context)


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data= request.POST)
     #   username = request.POST.get("username")
     #   password = request.POST.get("password")
     #   print(username, password)
     #   user = authenticate(request, username=username,password=password)
     #   if user is None:
     #       context = {"error":"Usuario o contraseña inválida"}
     #       return render(request,"cuentas_usuario/login.html",context)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm(request)
    context = {
        "form":form
    }
    return render(request,"cuentas_usuario/login.html",context)

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("/")
    return render(request,"cuentas_usuario/logout.html",{})
