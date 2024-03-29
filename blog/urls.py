from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('posts', views.post_list, name='post_list'),
    path('post/<int:pk>', views.post_detail, name='post_detail'),
    path('photos', views.PhotoListView.as_view(), name='photo_list'),
    path('photo/<int:pk>', views.photo_detail, name='photo_detail'),
    path('about', views.about, name='about')
]
