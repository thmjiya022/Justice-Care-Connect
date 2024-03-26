from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_page, name='register'),

    path('case/', views.case_list,name='case_list'),
    path('case/<int:case_id>/', views.case_detail, name='case_detail'),
    path('case/add/', views.add_case, name='add_case'),
    path('case/<int:case_id>/edit/', views.edit_case, name='edit_case'),

    
]