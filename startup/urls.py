from django.urls import path , include
from . import views
from . views import InvestorListView


urlpatterns = [

	# /startup/
    path('', views.startup, name='startup'), 
    # path('<int:pk>/',StartupDetailView.as_view(),name='startup-detail'),
    path('<int:pk>/',views.startupdetails,name='startup-detail'),
    path('startup_entity_submission/', views.startup_entity_submission, name='startup_entity_submission'),
    path('startup_founder_submission/', views.startup_founder_submission, name='startup_founder_submission'),
    path('startup_cofounder_submission/', views.startup_cofounder_submission, name='startup_cofounder_submission'),
    path('startup_video_submission/', views.startup_video_submission, name='startup_video_submission'),
    path('startup_deck_submission/', views.startup_deck_submission, name='startup_deck_submission'),
    path('startup_finan_submission/', views.startup_finan_submission, name='startup_finan_submission'),
    path('startup_funding_submission/',views.startup_funding_submission,name='startup_funding_submission'),
    path('plans/', views.plans, name='plans'),
    path('sprofile/', views.startup_own_profile, name='sprofile'),
    path('sopportunity/',InvestorListView.as_view(),name='startup_opportunity')

]