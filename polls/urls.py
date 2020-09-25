from django.urls import path
from . import views

urlpatterns = [
	path('', views.polls_display, name='polls_display'),
	path('<int:pk>/details/', views.polls_details, name='polls_details'),
	path('<int:pk>/results/', views.polls_results, name='polls_results'),
	path('<int:pk>/vote/', views.polls_vote, name='polls_vote'),
	path('edit/', views.polls_new, name='polls_new'),
	path('<int:pk>/edit/', views.polls_edit, name='polls_edit'),
]

