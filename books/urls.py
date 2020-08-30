from django.urls import path
from .views import HomePageView, DetailPageView, CreatePageView, UpdatePageView, DeletePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('post/<int:pk>', DetailPageView.as_view(), name='books'), 
    path('post/new', CreatePageView.as_view(), name='create'),
    path('post/<int:pk>/edit/', UpdatePageView.as_view(), name='update'),
    path('post/<int:pk>/delete/', DeletePageView.as_view(), name='delete'),
]