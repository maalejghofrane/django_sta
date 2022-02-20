from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponseRedirect
from .forms import ModuleRegistration
from .models import Module 
# Create your views here.

#fonction pour ajouter et afficher les modules
def add_show(request):
    if request.method == 'POST':
        fm = ModuleRegistration(request.POST)
        if fm.is_valid():
            tit = fm.cleaned_data['title']
            cf = fm.cleaned_data['coeff']
            sp = fm.cleaned_data['specialite']
            reg = Module(title=tit,coeff=cf, specialite=sp)
            reg.save()
    else:
        fm = ModuleRegistration()
    stud = Module.objects.all()
    return render(request, 'module/addandshow.html', {'form': fm, 'stu': stud})

    #Fonction Modifier un module 
def update_data(request, id): 
    if request.method=='POST':
     pi = Module.objects.get(pk=id)
     fm = ModuleRegistration(request.POST,instance=pi)
     if fm.is_valid(): 
         fm.save()
    else :
         pi = Module.objects.get(pk=id)
         fm = ModuleRegistration(instance=pi)
    return render(request,'module/updatemodule.html', {'form':fm})

    #Fonction supprimer un module 
def delete_data(request, id):
    if request.method == "POST":
        pi = Module.objects.get(pk=id)
        pi.delete()
    return HttpResponseRedirect('/modules')