from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.tracker,name='tracker'),
    path('day-description-form/',views.trackerForm,name='tracker-form')
]
