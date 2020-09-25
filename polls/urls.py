from django.urls import path
from . import views

urlpatterns = [
	path('', views.polls_display, name='polls_display'),
	path('details/<int:pk>/', views.polls_details, name='polls_details'),
	path('results/<int:pk>/', views.polls_results, name='polls_results'),
	path('vote/<int:pk>/', views.polls_vote, name='polls_vote'),
]

