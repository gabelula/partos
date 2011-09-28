from tastypie.resources import ModelResource
from births.models import Birth

class BirthResource(ModelResource):
    class Meta:
        queryset = Birth.objects.all()
        allowed_methods = ['get']
