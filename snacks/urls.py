from django.urls import path

from .views import HomePageView, AboutView

urlpatterns = [
     path('', HomePageView.as_view(), name = 'home'),
     path('aboutme', AboutView.as_view(), name = 'aboutme')
]