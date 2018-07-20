from django.urls import path

from . import views

app_name = 'members'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('post_list/', views.post_list, name='post_list'),
    path('logout/', views.logout_view, name='logout'),

]
