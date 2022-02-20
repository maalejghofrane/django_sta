from django.contrib import admin
from .models import Specialite

# Register your models here.
@admin.register(Specialite)
class UserAdmin(admin.ModelAdmin):
    list_display3 = ('titre','niveau')
