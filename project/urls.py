"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from etudiant import views 
from matiere import views as vs
from module import views as vs_md
from specialite import views as vs_sp
from note import views as vs_note
# from django.contrib.auth import views as auth_views
from users import views as vs_us

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.add_show, name = "addandshow"),
    path('delete/<int:id>/',views.delete_data, name="deletedata"),
    path('<int:id>/',views.update_data, name="updatedata"),

    path('matieres', vs.add_show, name = "addandshow_mat"),
    path('matiere/<int:id>/',vs.update_data, name="updatedataMatiere"),
    path('delete/matiere/<int:id>/',vs.delete_data, name="deletedata_matiere"),

    path('modules', vs_md.add_show, name = "addandshowModule"),
    path('modules/<int:id>/',vs_md.update_data, name="updatedataModule"),
    path('delete/module/<int:id>/',vs_md.delete_data, name="deletedataModule"),

    path('specialites', vs_sp.add_show, name = "addandshowSpecialites"),
    path('specialites/<int:id>/',vs_sp.update_data, name="updatedataSpecialites"),
    path('delete/specialite/<int:id>/',vs_sp.delete_data, name="deletedataSpecialites"),

    path('notes', vs_note.add_show, name = "addandshowNote"),
    path('notes/<int:id>/',vs_note.update_data, name="updatedataNote"),
    path('delete/note/<int:id>/',vs_note.delete_data, name="deletedataNote"),

    path('show_all', vs_note.show_all, name = "show_all"),

    # path('login/', auth_views.LoginView.as_view(templates_name='etudiant/login.html'), name = "login"),
    # path('logout/', auth_views.LogoutView.as_view(template_name='etudiant/logout.html'), name = "logout"),
    # path('login/', TemplateView.as_view(template_name='useres/login.html'))

    path('log', vs_us.login, name = "sho"),
    path('reg', vs_us.register, name='reg')


]
