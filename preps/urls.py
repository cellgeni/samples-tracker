from django.urls import path
from .views import SamplesListView, SamplesView, StagesListView, SamplesAutocomplete, StagesSearch

urlpatterns = [
    path('', SamplesView.as_view()),
    path('api/samples', SamplesListView.as_view()),
    path('api/samples/<str:sid>/stages', StagesSearch.as_view()),
    path('api/samples-search/', SamplesAutocomplete.as_view()),
]