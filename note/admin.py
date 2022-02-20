from django.contrib import admin
from .models import Note

# Register your models here.
@admin.register(Note)
class UserAdmin(admin.ModelAdmin):
    list_display2 = ('user','matiere','date_joined','note_ds','note_exam','note_tp')