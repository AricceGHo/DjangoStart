from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic.base import View
from .models import Build
# Create your views here.

class BuildView(View):
    def get(self, request):
        builds = Build.objects.all()
        return render(request, "builds/builds_list.html", {"builds_list": builds})

class BuildDetailView(View):
    def get(self,request,pk):
        build=Build.objects.get(id=pk)
        return render(request, "builds/build_detail.html", {"build": build})
