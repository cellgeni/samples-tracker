from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, RedirectView, TemplateView
from rest_framework import generics

from preps.models import CORE_PROJECTS, NON_CORE_PROJECTS, Project
from .models import Sample, Stage, Action, WarehouseSample, Owner, AgressoProject
from .serializers import SampleSerializer, StageSerializer, StageCreateSerializer


class HomePageView(RedirectView):
    url = "samples/"


class SamplesListView(View):
    template_name = "samples.html"

    def get(self, request, *args, **kwargs):
        context = {}
        projects = {}
        samples = WarehouseSample.objects.using("warehouse").raw(WarehouseSample.warehouse_view)
        new_samples = []
        for sample in samples:
            if sample.cost_code not in projects:
                projects[sample.cost_code] = Project.objects.get(cost_code=sample.cost_code)
            setattr(sample, "core", "Core" if projects[sample.cost_code].is_core else "Non-core")
            setattr(sample, "balance", projects[sample.cost_code].balance_avail)
            new_samples.append(sample)
        context['object_list'] = new_samples
        return render(request, self.template_name, context)


class ProjectView(View):
    template_name = "projects_list.html"

    def get(self, request, *args, **kwargs):
        context = {}
        cost_code = kwargs.get("cost_code")
        is_project_core = True
        object_list = AgressoProject.objects.using("agresso").raw(AgressoProject.core_view(cost_code))
        if len(list(object_list)) == 0:
            is_project_core = False
            object_list = AgressoProject.objects.using("agresso").raw(AgressoProject.non_core_view(cost_code))

        context['cost_code'] = cost_code
        context['object_list'] = object_list
        context['is_project_core'] = is_project_core
        if is_project_core:
            context['total'] = AgressoProject.total_balance(CORE_PROJECTS, cost_code)
        else:
            context['total'] = AgressoProject.total_balance(NON_CORE_PROJECTS, cost_code)
        return render(request, self.template_name, context)


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


class StageCreateView(generics.CreateAPIView):
    serializer_class = StageCreateSerializer


class SampleView(View):
    template_name = "single_sample.html"

    def get(self, request, *args, **kwargs):
        context = {}
        sid = kwargs.get("sid")
        try:
            sample = Sample.objects.get(sid=sid)
        except ObjectDoesNotExist:
            sample = Sample(sid=sid)
            sample.save()
        context['sid'] = sample.id
        context['actions'] = Action.objects.all()
        context['stages'] = Stage.objects.filter(sample=sample)
        context['owners'] = Owner.objects.all()
        return render(request, self.template_name, context)


class SamplesAutocomplete(View):

    def get(self, request, *args, **kwargs):
        q = request.GET.get('term', '')
        samples = AgressoProject.get_samples().objects.filter(sid__contains=q)
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
        context = {}
        sid = kwargs.get('sid')
        try:
            id = int(sid)
            sample = Sample.objects.get(id=id)
        except ValueError:
            sample = Sample.objects.get(sid=sid)
        context['sid'] = sid
        context['actions'] = Action.objects.all()
        context['stages'] = Stage.objects.filter(sample=sample)
        context['owners'] = Owner.objects.all()
        return render(request, self.template_name, context)


class SamplesSearch(ListView):
    template_name = 'samples_list.html'

    def get(self, request, *args, **kwargs):
        self.sid = request.GET.get('q')
        return super(SamplesSearch, self).get(self, request, *args, **kwargs)

    def get_queryset(self):
        return Sample.objects.filter(sid__contains=self.sid)
