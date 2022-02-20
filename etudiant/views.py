from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User 
# Create your views here.

#fonction pour ajouter et afficher les etudiants
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            ag= fm.cleaned_data['age']
            tel= fm.cleaned_data['tel']
            niv= fm.cleaned_data['niveau']
            spc= fm.cleaned_data['specialite']
            reg = User(name=nm,email=em, age=ag,tel=tel,niveau=niv,password=pw,specialite=spc)
            reg.save()
    else:
        fm = StudentRegistration()
    stud = User.objects.all()
    return render(request, 'etudiant/addandshow.html', {'form': fm, 'stu': stud})

    #Fonction Modifier un etudiant 
def update_data(request, id): 
    if request.method=='POST':
     pi = User.objects.get(pk=id)
     fm = StudentRegistration(request.POST,instance=pi)
     if fm.is_valid(): 
         fm.save()
    else :
         pi = User.objects.get(pk=id)
         fm = StudentRegistration(instance=pi)
    return render(request,'etudiant/updatestudent.html', {'form':fm})

    #Fonction supprimer un etudiant 
def delete_data(request, id):
    if request.method == "POST":
        pi = User.objects.get(pk=id)
        pi.delete()
    return HttpResponseRedirect('/')