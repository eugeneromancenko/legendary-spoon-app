from django.urls import path

from emailapi import views


urlpatterns = [
    # URL pattern that maps the root path to this view
    path('', views.home, name='home'),
    path('emails/', views.EmailList.as_view()),
    path('emails/<int:pk>/', views.EmailDetail.as_view()),
]
