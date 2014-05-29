"""
iOS device Model
class: Device
    Represents an iOS device with unique token.
    token = models.CharField(max_length=64, blank=False, null=False)
    is_active = models.BooleanField(default=True)
    deactivated_at = models.DateTimeField(null=True, blank=True)
    service = models.ForeignKey(APNService)
    users = models.ManyToManyField(getattr(settings, 'AUTH_USER_MODEL', 'auth.User'), null=True, blank=True, related_name='ios_devices')
    added_at = models.DateTimeField(auto_now_add=True)
    last_notified_at = models.DateTimeField(null=True, blank=True)
    platform = models.CharField(max_length=30, blank=True, null=True)
    display = models.CharField(max_length=30, blank=True, null=True)
    os_version = models.CharField(max_length=20, blank=True, null=True)
"""

from django.forms import widgets
from rest_framework import serializers
from ios_notifications.models import Device, APNService, BaseService

class IOSDeviceSerializer(serializers.Serializer):
	token			= serializers.CharField(required=True, max_length=64)
	is_active		= serializers.BooleanField(default=True)
	service			= serializers.CharField(APNService)
	platform		= serializers.CharField(max_length=30, required=False)
	display			= serializers.CharField(max_length=30, required=False)
	os_version		= serializers.CharField(max_length=30, required=False)


	def restore_object(slef, attrs, instance=None):
		"""
		Creates or updates a new iOS device instance, given a directory of desearialized
		field values.

		Note that if we don't define this method, then desearializing data will simply 
		return a dictionary of items.
		"""
		# update existing instance
		if instance:
			instance.token		= attrs.get('token', instance.token)
			instance.is_active	= attrs.get('is_active', instance.is_active)
			instance.service	= attrs.get('service', instance.service)
			instance.platform	= attrs.get('platform', instance.platform)
			instance.os_version	= attrs.get('os_version', instance.os_version)
		return Device(**attrs)

		class Model:
			model 	= Device
			fields	= ('token', 'is_active', 'service', 'platform', 'os_version')






