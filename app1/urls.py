from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from app1 import views

urlpatterns = [
    path('details/', views.DetailList.as_view()),
    path('show/<int:pk>/', views.AllDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
