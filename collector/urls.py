from django.urls import path
from . import views

#URL conf
urlpatterns = [
    path('map/', views.dispMap, name='map'),
    path('save_feature', views.save_feature, name='save_feature'),
]

