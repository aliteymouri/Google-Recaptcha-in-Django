from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'account'
urlpatterns = [
    path('log_in', views.LoginView.as_view(), name='log_in'),
    path('log_out', LogoutView.as_view(next_page='home:home'), name='log_out'),
]
