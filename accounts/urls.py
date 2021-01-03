from django.urls import path

from . import views
from .views import TopPageView

app_name = 'accounts'

urlpatterns = [
    path('', TopPageView.as_view(), name='toppage'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
]
