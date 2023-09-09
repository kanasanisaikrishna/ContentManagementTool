from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name ='index'),
    path('signin/',views.signin,name ='signin'),
    path('signup/',views.signup,name ='signup'),
    path('home/',views.home,name ='home'),
    path('add/',views.addBlog,name='addblog'),
    path('like/<str:pk>',views.likeBlog,name='like'),
    path('signout/',views.signout,name='signout'),
    path('myblog/',views.myblog,name='myblog'),
    path('delete/<str:pk>',views.deleteBlog,name='delete'),
    
]