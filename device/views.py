from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions

from ios_notifications.models import Device, APNService, BaseService, Notification
from device.serializers import IOSDeviceSerializer

class IOSDevice(APIView):
	"""
	<b>Lists all iOS Devices registered for ios_notifications</b>
	\n Created by - The Punjabi Devil
	"""
	def get(self, request, format=None):
		device 		= Device.objects.all()
		serializer 	= IOSDeviceSerializer(device, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer 		= IOSDeviceSerializer(data=request.DATA)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class IOSDeviceDetail(APIView):
	"""docstring for IOSDeviceDetail"""
	
	def get_object(self, pk):
		try:
			return Device.objects.get(pk=pk)
		except Device.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		#raise Http405
		print "I am inside the detail method"
		device 		= self.get_object(pk)
		serializer 	= IOSDeviceSerializer(device, data=request.DATA)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		device 		= self.get(pk)
		serializer 	= IOSDeviceSerializer(device)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		device 		= self.get_object(pk)
		device.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

class SendNotification(View):
	"""docstring for SendNotification"""

	def get(self, request, *args, **kwargs):
		device_tokens = ('2bfd049e06fad81809c488350188a02c38b2aae2d142805e48d643f29a2c063a')
		apns = APNService.objects.get(hostname='gateway.sandbox.push.apple.com', name='development')
		devices = Device.objects.filter(token='2bfd049e06fad81809c488350188a02c38b2aae2d142805e48d643f29a2c063a', service=apns)
		notification = Notification.objects.create(message='Message sent from Class View.', service=apns)
		apns.push_notification_to_devices(notification, devices, chunk_size=200)
		return HttpResponse("Check the device if you receive the Notification.")
		


