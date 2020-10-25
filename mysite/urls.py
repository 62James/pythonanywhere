from django.contrib import admin
from django.contrib.auth import views as aunt_views
from django.urls import path, include
from myweb import views

urlpatterns = [

   # path('', views.index, name='index'),
  # path('', views.index, name='index'),

    path('', aunt_views.LoginView.as_view(template_name='myweb/login.html'), name='login'),

   # path('login_active',views.login_active, name='login_active'),
    path('home',views.home, name='home'),
    path('logout',views.logout, name='logout'),
    path('recipes_details1',views.recipes_details1, name='recipes_details1'),
    path('recipes_details2',views.recipes_details2, name='recipes_details2'),
    path('recipes_details3',views.recipes_details3, name='recipes_details3'),
    path('recipes_details4',views.recipes_details4, name='recipes_details4'),
    path('recipes_details5',views.recipes_details5, name='recipes_details5'),
    path('recipes_details6',views.recipes_details6, name='recipes_details6'),
    path('myweb/',include('myweb.urls')),
    path('admin/',admin.site.urls),

]