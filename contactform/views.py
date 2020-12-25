from django.shortcuts import render, redirect
from .models import ContactForm
import datetime
# Create your views here.
def contact_add (request):

    now = datetime.datetime.now()
    year = now.year
    month = now.month
    day= now.day
    if len(str(day)) == 1:
        day = "0" +str(day)
    if len(str(month)) == 1:
        month = "0" + str(month)
    
    today = str(year) + "/" + str(month) + "/" + str(day) 
    time = str(now.hour) + ':' + str(now.minute)

    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        txt = request.POST.get('msg')

        if name == '' or email == '' or phone == '' or txt == '':
            message = 'All Fields are Required'
            return render(request,'msgbox.html',{'message':message})   

        b = ContactForm(name=name,email=email,phone=phone,txt=txt,date=today,time=time)
        b.save()
        message = 'Your Message has been Received'
        return render(request,'msgbox.html',{'message':message})     
    return render(request,'msgbox.html')

def contact_show (request):

    msg = ContactForm.objects.all()

    return render(request,'back/contactform.html',{'msg':msg})

def contact_del(request,pk):


    b = ContactForm.objects.filter(pk=pk)
    b.delete()

    return redirect ('contact_show')
