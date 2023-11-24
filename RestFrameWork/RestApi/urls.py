from django.urls import path

from . import views
from .views import (StudentGetPostList, StudentPutDelList, classgetpost,classget,
                    classputdel)

urlpatterns = [
    #Generic Urls-----------------------------------------------------------
    path('getuserapi/', classget.as_view()),
    path('getpostapi/', classgetpost.as_view()),
    path('putdelapi/<int:pk>', classputdel.as_view()),

    #Class Urls-------------------------------------------------------------
    path('Details/', StudentGetPostList.as_view(), name='Details'),
    path('Alter/<int:pk>/', StudentPutDelList.as_view(), name='Alter'),

    #Function Urls----------------------------------------------------------
    path('getapi/', views.getapi),
    path('postapi/', views.postapi),
    path('putapi/<pk>', views.putapi),
    path('deleteapi/<pk>', views.deleteapi),

    path('s3get/',views.s3get),
    
]