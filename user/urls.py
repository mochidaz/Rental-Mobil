from django.urls import path
from . import views

urlpatterns = [
	path('dashboard/', views.index, name='index_user'),
	path('signin/', views.signin, name='signin'),
	path('signup/', views.signup, name='signup'),
	path('signout/', views.signout, name='signout'),
]
