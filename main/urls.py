from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('data_butb/', views.form_data_butb, name='form_data'),
    path('delete_butb/', views.delete_butb, name='delete'),
    path('delete_all_butb/', views.delete_all_butb, name='delete_all'),
    path('complete_butb/', views.complete_butb, name='complete'),
    path('data_zaku/', views.form_data_zaku, name='form_data_zaku'),
    path('delete_all_zaku/', views.delete_all_zaku, name='delete_all_zaku'),
    path('complete_zaku/', views.complete_zaku, name='complete_zaku'),
    path('complete_all_zaku/', views.complete_all_zaku, name='complete_all_zaku'),
    path('ai_start/', views.ai_start_zaku, name='ai_start'),
    path('ai_start_butb/', views.ai_start_butb, name='ai_start_butb'),
]