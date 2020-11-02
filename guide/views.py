from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import GuideSerizlizer
from .models import Guide
from django.views.generic.base import View
from django.views.generic import ListView
from django.shortcuts import render, redirect
from .froms import GuideForm
from django.views.generic.edit import CreateView


# Create your views here.


class GuidList(APIView):
    def get(self, request):
        guide = Guide.objects.all()
        serializer = GuideSerizlizer(guide, many=True)
        return Response(serializer.data)


class GuideListShow(ListView):
    guide = Guide
    context_object_name = 'guide'
    template_name = 'main/guide_list.html'
    paginate_by = 5

    def get_queryset(self):
        guide = Guide.objects.all()
        return guide


class AddGuide(CreateView):
    form_class = GuideForm
    template_name = 'main/add_guide.html'
    success_url = '/success/'

    def form_valid(self, form):
        Guide.objects.create(**form.cleaned_data)
        return redirect('guide')