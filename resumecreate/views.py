from django.shortcuts import render , redirect
from .models import Personal , Education
from django.forms import modelformset_factory , inlineformset_factory
# Create your views here.


def personal_add (request):

    

    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        add = request.POST.get('address')
        city = request.POST.get('city')
        pin = request.POST.get('pin')
        country = request.POST.get('country')
        phn = request.POST.get('phnno')
        eml = request.POST.get('email')
        objective = request.POST.get('objective')

        if fname == '' or lname =='' or eml == '' or add ==''or city ==''or pin =='' or country =='' or phn == '' or objective == '':
            message = 'All Fields are Required'
            return render(request,'msgbox.html',{'message':message})   

        b = Personal(fname=fname,eml=eml,phn=phn,objective=objective,lname=lname,add=add,city=city,pincode=pin,country=country)
        b.save()
        return redirect('education_add',pk = personal.id)     
    return render(request,'msgbox.html')


def education_add(request,pk):

    personal = Personal.objects.get(pk=pk)
    #EducationFormset = modelformset_factory(Education,fields=('institution','degree','startdate','enddate',))
    EducationFormset = inlineformset_factory(Personal,Education,fields=('institution','degree','startdate','enddate',),extra=1)

    if request.method == 'POST':
        #formset = EducationFormset(request.POST , queryset=Education.objects.filter(personal__id=personal.id))
        formset = EducationFormset(request.POST , instance=personal)
        if formset.is_valid():
            formset.save()
            #instances = formset.save(commit=False)
            #for instance in instances :
            #    instance.personal_id = personal.id
             #   instance.save()

            return redirect('education_add',pk = personal.id)

    #formset = EducationFormset(queryset=Education.objects.filter(personal__id=personal.id))
    formset = EducationFormset(instance=personal)
    return render(request, 'education.html',{'formset':formset})