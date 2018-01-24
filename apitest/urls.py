from django.conf.urls import url,patterns
from apitest.views import *

urlpatterns = patterns('',
	url(r'^user/$',UserView.as_view(),name = 'crud_user'),
	url(r'^task/$',TaskView.as_view(),name = 'crud_task'),
)
