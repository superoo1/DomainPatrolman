

from rest_framework.generics import  ListAPIView,RetrieveAPIView
from .models import WebSite
from .serialization import DomainlistSerializer



class ApiDomainlist(ListAPIView):
    queryset = WebSite.objects.all()
    serializer_class = DomainlistSerializer
    pass




class ApiWebcheckView(RetrieveAPIView):
    model = WebSite



    pass
