from django.contrib import admin
from .models import Module
# Register your models here.

@admin.register(Module)
class UserAdmin(admin.ModelAdmin):
    list_display2 = ('title','coeff','Specialite')