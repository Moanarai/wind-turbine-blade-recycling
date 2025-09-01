from django.conf import settings
from django.urls import path
from ad_min import views
from django.conf.urls.static import static


urlpatterns = [

    # home page......................

    path('', views.home, name='home'),

    # Admin login and logout.......................

    path('adminlogin/', views.adminlogin, name='adminlogin'),
    path('logout/', views.logout, name='logout'),

     # admin home..........................

    path('adminhome/', views.adminhome, name='adminhome'),


    # admin requirements...................................................

    path('requirements/', views.requirements, name='requirements'),

    # admin approve tables for all modules...............................

    path('solvoapprove/', views.solvoapprove, name='solvoapprove'),
    path('recapprove/', views.recapprove, name='recapprove'),
    path('fabricapprove/', views.fabricapprove, name='fabricapprove'),
    path('assessapprove/', views.assessapprove, name='assessapprove'),
    

    # admin manage tables for all modules...............................

    path('solvomanage/', views.solvomanage, name='solvomanage'),
    path('recmanage/', views.recmanage, name='recmanage'),
    path('fabricmanage/', views.fabricmanage, name='fabricmanage'),
    path('assessmanage/', views.assessmanage, name='assessmanage'),
  

    #manage status...............................................

    path('managestatus/', views.managestatus, name='managestatus'),

    # admin approve and reject.......................................

    path('approve/<int:id>/', views.approve, name='approve'),
    path('reject/<int:id>/', views.reject, name='reject'),

    # generate report .............................................

    path('final_report/<str:project_id>/', views.final_report, name='final_report'),


    


 ]

urlpatterns += static(settings.MEDIA_URL,document_root=settings
 .MEDIA_ROOT)