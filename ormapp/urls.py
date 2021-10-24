"""ormproject URL Configuration

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
from .import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',v.home),
    path('addstudent',v.add_student),
    path('addemp',v.add_emp),
    path('addaccount',v.add_account),
    path('emplist',v.emp_list),
    path('studentlist',v.student_list),
    path('accountlist',v.account_list),
    path('deleteEmp',v.delete_Emp1),
    path('editEmp/<str:email>',v.edit_Emp),
    path('deleteEmp/<str:email>',v.delete_Emp2),
    path('deleteAcc',v.delete_Acc),
    #path('editAcc',v.edit_Acc),
    path('deleteAcc/<int:id>',v.delete_Acc2),
    path('addqualif',v.add_qualif),
    path('adduser1',v.add_user1),
    path('adduser2',v.add_user2),
    path('adduser3',v.add_user3),
    path('adduser4',v.add_user4),
    path('adduser5',v.add_user5),
    path('adduser6',v.add_user6),

    path('addsinger',v.add_singer),
    path('addsongs',v.add_songs),
    path('singerlist',v.singer_list),
    path('songslist',v.songs_list),

]
