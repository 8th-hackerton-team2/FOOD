from django.urls import path
from food import views


app_name = 'food'

urlpatterns = [
    path('post_list/', views.post_list, name='post_list'),
    path('post_detail/<int:pk>/', views.post_detail, name='post_detail'),
]
