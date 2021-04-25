from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('',views.log,name='log'),
    path('logout/', views.logoutUser, name="logout"),
    path('adminhome/',views.adhome,name='adminHome'),
    path('student_registration/',views.student_reg,name='student-registration'),
    path('student_list/',views.student_detail,name='student-list'),
    path('view/<str:pk>/', views.stud_info, name='viewpage'),
    path('delete/<str:pk>/',views.delete,name='deleteuser'),
    path('update/<str:pk>/', views.update, name='updatepage'),
    path('updatesem1/<str:pk>/', views.updatesem1, name='updatesem1'),
    path('updatesem2/<str:pk>/', views.updatesem2, name='updatesem2'),
    path('updatesem3/<str:pk>/', views.updatesem3, name='updatesem3'),
    path('updatesem4/<str:pk>/', views.updatesem4, name='updatesem4'),
    path('updatesem5/<str:pk>/', views.updatesem5, name='updatesem5'),
    path('event_home/', views.eventhome, name='eventhome'),
    path('update_event/', views.event_reg, name='eventreg'),
    path('event_view/', views.event_view, name='eventview'),
    path('staffreg/',views.staffreg,name='staffreg'),
    path('staffhome/', views.sthome, name='staffHome'),
    path('detailhome/',views.staffview,name='detailhome'),
    path('staffdetail/<str:pk>',views.indview,name='view'),
    path('detailview/',views.view,name='staffview'),
    path('staffupdate/',views.updatestaff,name='staffupdate'),
    path('educationupdate/',views.educationupdate,name='educationupdate'),
    path('oeupdate/',views.oeupdate,name='oeupdate'),
    path('apupdate/',views.apupdate,name='apupdate'),
    path('articleupdate/',views.articleupdate,name='articleupdate'),
    path('seminarupdate/',views.seminarupdate,name='seminarupdate'),
    path('reset-password/',auth_views.PasswordResetView.as_view(template_name='passreset.html'),name="reset_password"),
    path('reset-password-sent/', auth_views.PasswordResetDoneView.as_view(template_name='passwordresetsent.html'), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='passresetform.html'),name="password_reset_confirm"),
    path('reset-password-done/', auth_views.PasswordResetCompleteView.as_view(template_name='passresetdone.html'),name="password_reset_complete"),

]