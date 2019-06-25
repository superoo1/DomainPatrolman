
from rest_framework.serializers import ModelSerializer
from .models import WebSite

class DomainlistSerializer(ModelSerializer):

    class Meta:
        model =WebSite
        fields = "__all__"


class WebsiteCheckSerializer(ModelSerializer):

    class Meta:
        model = WebSite
        fields = "__all__"
















