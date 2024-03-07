from django.urls import path
import . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('schedule/', views.schedule, name='schedule'),
    path('speakers/', views.speakers, name='speakers'),
    path('venue/', views.venue, name='venue'),
]
