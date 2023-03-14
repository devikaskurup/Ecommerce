from django.urls import path
from .import views

urlpatterns = [
      path("",views.index,name='index'),
      path('SignIn',views.SignIn,name='SignIn'),
      path('SignUp',views.SignUp,name='SignUp'),
      path("signout",views.SignOut,name="SignOut"),
      path("AdminIndex",views.AdminIndex,name="AdminIndex"),
]
