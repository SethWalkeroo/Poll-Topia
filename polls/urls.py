from django.urls import path
from . import views

urlpatterns = [
	path('', views.polls_display, name='polls_display'),
	path('poll/<int:pk>/', views.polls_details, name='polls_details'),
]