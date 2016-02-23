from tastypie.resources import ModelResource
from account.models import MyModel
class MyModelResource(ModelResource):
    class Meta:
        queryset = MyModel.objects.all()
	resource_name = 'mymodel'
        allowed_methods = ['post', 'get', 'patch', 'delete']
               
