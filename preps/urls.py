from django.urls import path

from .views import SamplesAPIListView, SamplesListView, SamplesAutocomplete, StagesSearch, SampleView, SamplesSearch

urlpatterns = [
    path('', SamplesListView.as_view()),
    path('samples/<str:sid>', SampleView.as_view()),
    path('api/samples', SamplesAPIListView.as_view()),
    path('api/samples-search/', SamplesSearch.as_view()),
    path('api/samples/<str:sid>/stages', StagesSearch.as_view()),
    path('api/samples-autocomplete/', SamplesAutocomplete.as_view()),
]
