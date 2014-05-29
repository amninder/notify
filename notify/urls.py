from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'notify.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('test_module.urls', namespace='test_module')),

    url(r'^devices/', include('device.urls', namespace='device')),

    url(r'^admin/', include(admin.site.urls)),
    #Django Registration URL
    (r'^accounts/', include('registration.backends.default.urls')),
    url(r'^ios-notifications/', include('ios_notifications.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)
