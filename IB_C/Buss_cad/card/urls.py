from django.urls import path
from . import views


urlpatterns =[
    path('', views.home, name='home'),
    # path('download-business-card/', views.download_business_card, name='download_business_card'),
]