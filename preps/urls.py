from django.urls import path

from .views import *

urlpatterns = [
    path('', HomePageView.as_view()),
    path('samples/', SamplesListView.as_view()),
    path('projects/', ProjectsListView.as_view()),
    path('samples/<str:sid>', SampleView.as_view()),
    path('api/samples', SamplesAPIListView.as_view()),
    path('api/samples-search/', SamplesSearch.as_view()),
    path('api/samples/<str:sid>/stages', StagesSearch.as_view()),
    path('api/samples-autocomplete/', SamplesAutocomplete.as_view()),
    path('api/stage/', StageCreateView.as_view()),
]
