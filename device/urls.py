from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns
from ios_notifications.models import Device, APNService, BaseService
from device import views

urlpatterns		= patterns( 'device.views',
		url(r'^ios/$', views.IOSDevice.as_view()),
		url(r'^ios/(?P<pk>[0-9]+)/$', views.IOSDeviceDetail.as_view()),
		url(r'^send/$', views.SendNotification.as_view()),
	)
urlpatterns = format_suffix_patterns(urlpatterns)