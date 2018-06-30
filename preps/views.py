from django.http import JsonResponse
from django.views import View
from django.views.generic import ListView
from rest_framework import generics

from .models import Sample, Stage
from .serializers import SampleSerializer, StageSerializer


class SamplesListView(ListView):
    template_name = "samples.html"

    def get_queryset(self):
        return Sample.objects.all()


class SamplesAPIListView(generics.ListAPIView):
    serializer_class = SampleSerializer
    queryset = Sample.objects.all()


class StagesListView(generics.ListAPIView):
    serializer_class = StageSerializer

    def get(self, request, *args, **kwargs):
        self.sid = kwargs.get('sid')
        return super(StagesListView, self).get(self, request, *args, **kwargs)

    def get_queryset(self):
        return Stage.objects.filter(sample__id=self.sid)


class SampleView(ListView):
    template_name = "single_sample.html"

    def get(self, request, *args, **kwargs):
        self.sid = kwargs.get('sid')
        return super(SampleView, self).get(self, request, *args, **kwargs)

    def get_queryset(self):
        return Stage.objects.filter(sample__sid=self.sid)


class SamplesAutocomplete(View):

    def get(self, request, *args, **kwargs):
        q = request.GET.get('term', '')
        samples = Sample.objects.filter(sid__contains=q)
        results = []
        for sample in samples:
            sample_json = {}
            sample_json['id'] = sample.id
            sample_json['label'] = sample.sid
            sample_json['value'] = sample.sid
            results.append(sample_json)
        return JsonResponse(results, safe=False)


class StagesSearch(ListView):
    template_name = 'single_sample_stages.html'

    def get(self, request, *args, **kwargs):
        self.sid = kwargs.get('sid')
        return super(StagesSearch, self).get(self, request, *args, **kwargs)

    def get_queryset(self):
        return Stage.objects.filter(sample__sid=self.sid)


class SamplesSearch(ListView):
    template_name = 'samples_list.html'

    def get(self, request, *args, **kwargs):
        self.sid = request.GET.get('q')
        return super(SamplesSearch, self).get(self, request, *args, **kwargs)

    def get_queryset(self):
        return Sample.objects.filter(sid__contains=self.sid)
