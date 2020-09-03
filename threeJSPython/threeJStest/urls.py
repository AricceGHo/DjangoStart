from django.urls import path
from . import views

urlpatterns = [
    path("", views.BuildView.as_view()),
    path("<int:pk>/", views.BuildDetailView.as_view()),
]