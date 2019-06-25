
from django.conf.urls import url,include
from .. import views

app_name = "monitor"

urlpatterns = [
    url(r'domain$',views.Tasks.as_view(),name="domins"),
    url(r'domainlist$', views.DomainList.as_view(), name="dominlist")

]


