from django.shortcuts import get_object_or_404,render_to_response
from django.http import HttpResponse
from django.conf.urls import include,patterns, url
from django.contrib.auth.models import User
from django.core.management import call_command
from account import views
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
#from account.models import Category,About, Register 
import json
import subprocess
import sys
import os
import python
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

def test_rest(request):
    para=  request.GET.get('parameter')
    #os.system('python python.py')
    p = subprocess.Popen("./scr.sh "+para,shell=True,stderr=subprocess.STDOUT,stdout=subprocess.PIPE,close_fds=True)
    a=p.stdout.read()
    print a
    message=a
    data = json.dumps({"username":message})
    return HttpResponse(data, content_type='application/json')

class TestView(APIView):
    renderer_classes = (JSONRenderer, )
    def get(self, request):
        content = {'username': 'testing'}
        return Response(content)
#       return Response(content)
# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^test/$',test_rest, name='test_rest'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
urlpatterns += patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    #url(r'^category/(?P<category_name_url>\w+)$', views.category, name='category'),
    #url(r'^add_category/$', views.add_category, name='add_category'),
    #url(r'^category/(?P<category_name_url>\w+)/add_page/$', views.add_page, name='add_page'),
    url(r'^register/$', views.register, name='register'), # ADD NEW PATTERN!
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^pid/$', views.pid, name='pid'),
 #   url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
#    url(r'^test/$', test_rest , name='test_rest'),
)
