from django.forms import widgets
from rest_framework import serializers
from test_module.models import TestModel

class TestSerializer(serializers.Serializer):
	pk 				= serializers.Field()
	message			= serializers.CharField(required=False, max_length=1000)

	def restore_object(self, attrs, instance=None):
		"""
		Creates or updates a new message instance, given a directory
		of desearialized field values.

		Note that if we don't define this method, then deserializing
		data will simply return a dictionary of items.
		"""
		if instance:
			# update existing instance
			instance.message	=attrs.get('message', instance.message)
		return TestModel(**attrs)
	class Model:
		model 		= TestModel
		fields		= ('pk', 'message')