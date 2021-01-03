from django.urls import path

from post import views

app_name = 'post'
urlpatterns = [
    path('post', views.TemplateView.as_view(), name='postview')

]
