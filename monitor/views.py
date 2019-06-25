from django.shortcuts import render

# Create your views here
from django.views.generic import TemplateView,ListView
from .models import WebSite

from .tasks import init_task
class Tasks(TemplateView):
    template_name = 'index.html'
    # init_task()
    pass


class DomainList(ListView):
    template_name = 'newdomain_list.html'
    queryset = WebSite.objects.all()




























