from django.conf.urls import url,include
from ..apiviews import  ApiDomainlist,ApiWebcheckView
app_name = 'monitor'

urlpatterns = [
   url(r'domainlist$',ApiDomainlist.as_view(),name = 'api-domainlist'),
   url(r'website/(?P<pk>[0-9a-zA-Z\-]{1,36})/check/$',ApiWebcheckView.as_view(),name="api-webcheck" )

   # url(r'rentbills$',ApiRentbill.as_view(),name = 'api-rentbills'),
   # url(r'store/citycount$', StoreCitycount.as_view(), name='api-citycount')

]







