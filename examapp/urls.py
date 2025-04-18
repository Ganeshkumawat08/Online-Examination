from django.urls import path
from . import views

urlpatterns = [
    path('home',views.home),
    path('about',views.about),
    path('contact',views.contact),
    
    path('signup',views.signup),
    path('login',views.login),

    path('user/<int:id>',views.user),
    path('updateuser/<int:id>',views.updateuser),

    path('viewusers',views.viewusers),
    path('checkuser/<int:id>',views.checkuser),
    
    path('adminlogin',views.adminlogin),
    path('admin/<int:id>',views.admin),

    path('courses',views.courses),
    path('addcourse',views.addcourse),
    path('editcourse/<int:id>',views.editcourse),

    path('subjects',views.subjects),
    path('addsubject',views.addsubject),
    path('editsubject/<int:id>',views.editsubject),

    path('paper',views.paper),
    path('addpaper',views.addpaper),
    path('editpaper/<int:id>',views.editpaper),
    path('subjectpaper/<int:id>',views.subjectpaper),    
    
    path('delete/<str:modelname>/<int:id>',views.delete),

    path('examcourse/<int:cid>/<int:id>',views.examcourse),
    path('examsubject/<int:sid>/<int:id>',views.examsubject),

    path('question/<str:subject>/<int:id>',views.question),

    path('resultcourse/<int:id>',views.resultcourse),
    path('resultsubject/<int:id>',views.resultsubject),
    path('examresult/<int:id>',views.examresult),
    path('allresults',views.results),

    # path('applycourse',views.applycourse)
]