from django.http import JsonResponse
from django.views import View
from django.views.generic import TemplateView, ListView
from rest_framework import generics

from .models import Sample, Stage
from .serializers import SampleSerializer, StageSerializer


class SamplesView(TemplateView):
    template_name = "samples.html"

    def get_context_data(self, **kwargs):
        context = dict()
        context["samples"] = Sample.objects.all()
        return context


class SamplesListView(generics.ListAPIView):
    serializer_class = SampleSerializer
    queryset = Sample.objects.all()


class StagesListView(generics.ListAPIView):
    serializer_class = StageSerializer

    def get(self, request, *args, **kwargs):
        self.sid = kwargs.get('sid')
        return super(StagesListView, self).get(self, request, *args, **kwargs)

    def get_queryset(self):
        return Stage.objects.filter(sample__id=self.sid)


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
    template_name = 'content.html'

    def get(self, request, *args, **kwargs):
        self.sid = kwargs.get('sid')
        return super(StagesSearch, self).get(self, request, *args, **kwargs)

    def get_queryset(self):
        return Stage.objects.filter(sample__sid=self.sid)
