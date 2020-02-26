from django.urls import path , include
from . import views
from . views import StartupListView 

urlpatterns = [ 

	# /investor/
    path('', views.investor, name='investor'),
    path('<int:pk>/',views.Investordetails,name='investor-detail'),
    path('investor_detail_submission/', views.investor_detail_submission, name='investor_detail_submission'),
    path('investor_thesis_submission/', views.investor_thesis_submission, name='investor_thesis_submission'),
    path('idetail/', views.investor_own_profile, name='idetail'),
    path('iopportunity/',StartupListView.as_view(),name='investor_opportunity'),
    

]