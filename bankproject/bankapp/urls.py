from django.urls import path
from . import views

app_name='bankapp'
urlpatterns = [
    path('dependantfield',views.dependantfield,name='dependantfield'),
    path('',views.home,name='home'),
    path('thrissur/',views.thrissur,name='thrissur'),
    path('ernakulam/',views.ernakulam,name='ernakulam'),
    path('kannur/',views.kannur,name='kannur'),
    path('kottayam/',views.kottayam,name='kottayam'),
    path('kollam/',views.kollam,name='kollam'),
    path('log/',views.log,name='log'),
    path('details/',views.details,name='details'),
    path('registers', views.registers, name='registers'),
    path('logout',views.logout,name='logout'),


        ]