from django.shortcuts import render , get_object_or_404,redirect  #404 for ,when we dont have database can we can handle it without showing 404
from .models import Main
from django.contrib.auth import authenticate,login,logout
from contactform.models import ContactForm
from django.core.mail import send_mail
from django.conf import settings 
# Create your views here.

def home (request):
    site = Main.objects.get(pk=1)
    return render(request,'index.html',{'site':site})

def contact(request):
    site = Main.objects.get(pk=1)
    return render(request,'contact.html',{'site':site})

def resume(request):
    site = Main.objects.get(pk=1)

    return render(request,'resume.html',{'site':site})


def services(request):
    site = Main.objects.get(pk=1)
    return render(request,'services.html',{'site':site})

def about(request):
    site = Main.objects.get(pk=1)
    return render(request,'about.html',{'site':site})

def resumesingle(request):
    site = Main.objects.get(pk=1)
    return render(request,'resume-single.html',{'site':site})

def panel(request):

    #login check start
    if not request.user.is_authenticated :
        return redirect('my_login')
    # login check end    

    site = Main.objects.get(pk=1)
    return render(request,'back/panel.html',{'site':site})

def my_login(request):

    if request.method == 'POST':

        utxt = request.POST.get('username')
        ptxt = request.POST.get('password')

        if utxt != "" and ptxt != "":
            user = authenticate(username=utxt,password=ptxt)

            if user != None :
                login(request, user)
                return redirect('panel')

    return render( request, 'login.html')

def my_logout (request):

    logout(request)

    return redirect('my_login')

def answer_cm(request,pk):

    if request.method =='POST':
        txt = request.POST.get('txt')

        if txt == '':
            error = "Type Your Answer.."
            return render(request, 'back/error.html',{'error':error})
        
        to_email = ContactForm.objects.get(pk=pk).email
        email_from = settings.EMAIL_HOST_USER 
        send_mail(
            'testing mails ',
            txt,
            email_from,
            [to_email],
            fail_silently = False,
        )

    return render(request,'back/answer_cm.html',{'pk':pk})


   
    




