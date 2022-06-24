from django.urls import path
from .views import HomePageView, HomeDetailView, HomeCreateView, HomeUpdateView, HomeDeleteView

urlpatterns = [
    path('new/<int:pk>/delete/', HomeDeleteView.as_view(),name='delete_post'),
    path('new/<int:pk>/edit', HomeUpdateView.as_view(),name='renew_post'),
    path('post/new/',HomeCreateView.as_view(), name="new_post"),
    path("",HomePageView.as_view(),name = "home"),  
    path('new/<int:pk>/', HomeDetailView.as_view(),name='home_detail'),
]

