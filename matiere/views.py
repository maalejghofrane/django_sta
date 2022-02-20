from django.shortcuts import render, HttpResponseRedirect
from .forms import MatiereRegistration
from .models import Matiere 

# Create your views here.

#fonction pour ajouter et afficher les matieres
def add_show(request):
    if request.method == 'POST':
        fm = MatiereRegistration(request.POST)
        if fm.is_valid():
            tit = fm.cleaned_data['titre']
            ds = fm.cleaned_data['ds']
            ex = fm.cleaned_data['exam']
            tp= fm.cleaned_data['tp']
            cf= fm.cleaned_data['coeff']
            mt = fm.cleaned_data['module']
            reg = Matiere(titre=tit,ds=ds, exam=ex,tp=tp,coeff=cf,module=mt)
            reg.save()
    else:
        fm = MatiereRegistration()
    stud = Matiere.objects.all()
    return render(request, 'matiere/addandshow.html', {'form': fm, 'stu': stud})


    #Fonction Modifier une matiére 
def update_data(request, id): 
    if request.method=='POST':
     pi = Matiere.objects.get(pk=id)
     fm = MatiereRegistration(request.POST,instance=pi)
     if fm.is_valid(): 
         fm.save()
    else :
         pi = Matiere.objects.get(pk=id)
         fm = MatiereRegistration(instance=pi)
    return render(request,'matiere/updatematiere.html', {'form':fm})

    #Fonction supprimer un etudiant 
def delete_data(request, id):
    if request.method == "POST":
        pi = Matiere.objects.get(pk=id)
        pi.delete()
    return HttpResponseRedirect('/matieres')