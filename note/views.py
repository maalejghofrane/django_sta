from django.shortcuts import render
from django.shortcuts import render, HttpResponseRedirect
from .forms import NoteRegistration
from .models import Note 
# Create your views here.

#fonction pour ajouter et afficher les notes
def add_show(request):
    if request.method == 'POST':
        fm = NoteRegistration(request.POST)
        if fm.is_valid():
            us = fm.cleaned_data['user']
            mt = fm.cleaned_data['matiere']
            ds = fm.cleaned_data['note_ds']
            tp = fm.cleaned_data['note_tp']
            exam = fm.cleaned_data['note_exam']
            x= 0.2*ds+0.5*exam+0.3*tp
            reg = Note(user=us,matiere=mt, note_ds=ds,note_tp=tp,note_exam=exam,moy=x)
            reg.save()
    else:
        fm = NoteRegistration()
    stud = Note.objects.all()
    return render(request, 'note/addandshow.html', {'form': fm, 'stu': stud})

 #Fonction Modifier une note 
def update_data(request, id): 
    if request.method=='POST':
     pi = Note.objects.get(pk=id)
     fm = NoteRegistration(request.POST,instance=pi)
     if fm.is_valid():
        us = fm.cleaned_data['user']
        mt = fm.cleaned_data['matiere']
        ds = fm.cleaned_data['note_ds']
        tp = fm.cleaned_data['note_tp']
        exam = fm.cleaned_data['note_exam']
        x= 0.2*ds+0.5*exam+0.3*tp
        reg = Note(user=us,matiere=mt, note_ds=ds,note_tp=tp,note_exam=exam,moy=x)
        pi.delete()
        reg.save()
    else :
         pi = Note.objects.get(pk=id)
         fm = NoteRegistration(instance=pi)
    return render(request,'note/updatenote.html', {'form':fm})

#Fonction supprimer un note 
def delete_data(request, id):
    if request.method == "POST":
        pi = Note.objects.get(pk=id)
        pi.delete()
    return HttpResponseRedirect('/notes')




#fonction pour ajouter et afficher les notes
def show_all(request):
    stud = Note.objects.all()
    return render(request, 'note/showAllNotes.html', {'stu': stud ,})