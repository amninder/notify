from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from test_module import views

urlpatterns 	= patterns('test_module.views',
	url(r'^messages/$', views.MessageList.as_view()),
	url(r'^messages/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
	)

urlpatterns = format_suffix_patterns(urlpatterns)