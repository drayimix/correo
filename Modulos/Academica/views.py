from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

#formulario
def formularioContacto(request):
    return render(request, "formularioContacto.html")

#resivir datos
def contactar(request):
    if request.method == "POST":
        asunto = request.POST["txtAsunto"]
        mensaje = request.POST["txtMensaje"] + " /Email: " + request.POST["txtEmail"]
        email_desde = settings.EMAIL_HOST_USER
        email_para = ["rincon77789@gmail.com"]
        send_mail(asunto, mensaje, email_desde, email_para, fail_silently=False)
        return render(request, "conactoExitoso.html")
    return render(request, "formularioContacto.html")