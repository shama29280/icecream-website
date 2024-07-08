from django.urls import path
from app import views
urlpatterns = [
   path('',views.index,name="index"),
   path('video',views.video,name="video"),
   path('video1',views.video1,name="video1"),
   path('video2',views.video2,name="video2"),
   path('order',views.order,name="order"),
   path('signup',views.handlesignup,name="handlesignup"),
   path('login',views.handlelogin,name="handlelogin"),
   path('logout',views.handlelogout,name="handlelogout"),
]