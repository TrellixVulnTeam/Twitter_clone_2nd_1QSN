from django.urls import path

from post import views

app_name = 'post'
urlpatterns = [
    path('', views.PostView.as_view(), name='post'),
    path('user_detail/', views.UserDetailView.as_view(), name="userdetail")
]
