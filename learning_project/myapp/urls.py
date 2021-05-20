from django.conf.urls import url
from myapp import views

app_name = "myapp"

urlpatterns = [
	url('register/', views.register, name='register'),
	url('user_login/', views.user_login, name='user_login'),
]