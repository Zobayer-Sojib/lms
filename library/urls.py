from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('show/', views.show, name='showdata'),
    path('searchhistory/', views.searchhistory, name='searchhistory'),
    path('search/', views.search, name='search'),
    path('add/', views.addinfo, name='insert'),
    path('editndel/', views.editinfondelete, name='editndel'),
    path('edit/<id>/', views.edit, name='edit'),
    path('update/<id>/', views.update, name='update'),
    path('delete/<id>/',views.delete, name='delete' ),
    path('book', views.bookList, name='bookList'),
    path('order', views.order, name='order'),
    path('register', views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("next", views.next, name="next"),
    path("logout", views.logout_request, name= "logout"),
   
    
]
