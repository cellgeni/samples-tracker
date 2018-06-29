from django.urls import path
from .views import SamplesListView, SamplesView, StagesListView, SamplesSearch, StagesSearch

urlpatterns = [
    path('', SamplesView.as_view()),
    path('api/samples', SamplesListView.as_view()),
    path('api/samples/<str:sid>/stages', StagesSearch.as_view()),
    path('api/samples-search/', SamplesSearch.as_view()),
]