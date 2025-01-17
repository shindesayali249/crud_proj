from django.urls import path
from . import views

urlpatterns = [
    path('reg/', views.register_view, name='reg_url'),
    path('login/', views.login_view, name='login_url'),
    path('logout/', views.logout_view, name='logout_url')
]