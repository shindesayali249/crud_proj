from django.urls import path
from .import views

urlpatterns = [
    path('add_stu/', views.add_stu_view, name='add_stu_url'),
    path('add_sub/', views.add_sub_view, name='add_sub_url'),
    path('show_stu/', views.show_stu_view, name='show_stu_url'),
    path('show_sub/', views.show_sub_view, name='show_sub_url'),
    path('update_stu/<pk>/', views.update_stu_view, name='update_stu_url'),
    path('update_sub/<pk>/', views.update_sub_view, name='update_sub_url'),
    path('delete_stu/<pk>/', views.delete_stu_view, name='delete_stu_url'),
    path('delete-sub/<pk>/', views.delete_sub_view, name='delete_sub_url')
]