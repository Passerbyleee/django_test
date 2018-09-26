from django.contrib import admin
from django.urls import path
from . import views
app_name='blog'
urlpatterns = [
    path('',views.index,name='index'),
    path('article/<int:id>',views.article,name='article'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('edit_function/',views.edit_function,name='edit_function')
]
