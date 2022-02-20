from django.shortcuts import render
from django.shortcuts import render, HttpResponseRedirect
from .forms import SpecialiteRegistration
from .models import Specialite 
# Create your views here.

#fonction pour ajouter et afficher les specialites
def add_show(request):
    if request.method == 'POST':
        fm = SpecialiteRegistration(request.POST)
        if fm.is_valid():
            tit = fm.cleaned_data['titre']
            nv = fm.cleaned_data['niveau']
            reg = Specialite(titre=tit,niveau=nv)
            reg.save()
    else:
        fm = SpecialiteRegistration()
    stud = Specialite.objects.all()
    return render(request, 'specialite/addandshow.html', {'form': fm, 'stu': stud})

#Fonction Modifier une specialité  
def update_data(request, id): 
    if request.method=='POST':
     pi = Specialite.objects.get(pk=id)
     fm = SpecialiteRegistration(request.POST,instance=pi)
     if fm.is_valid(): 
         fm.save()
    else :
         pi = Specialite.objects.get(pk=id)
         fm = SpecialiteRegistration(instance=pi)
    return render(request,'specialite/updatespecialite.html', {'form':fm})

#Fonction supprimer une spécialité 
def delete_data(request, id):
    if request.method == "POST":
        pi = Specialite.objects.get(pk=id)
        pi.delete()
    return HttpResponseRedirect('/specialites')