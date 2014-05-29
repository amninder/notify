from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions

from test_module.models import TestModel
from test_module.serializers import TestSerializer


class JSONResponse(HttpResponse):
	"""
	JSONResponse renders it's content into JSON
	"""
	def __init__(self, data, **kwargs):
		content		= JSONRenderer().render(data)
		kwargs['content_type'] = 'application/json'
		super(JSONResponse, self).__init__(content, **kwargs)


#Now we dont need JSONResponse
class MessageList(APIView):
	"""
	<b>Lists all messages</b>\n
	Created by - Amninder S Narota
	"""
	#permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
	def get(self, request, format=None):
		messages  	= TestModel.objects.all()
		serializer 	= TestSerializer(messages, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer 	= TestSerializer(data=request.DATA)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SnippetDetail(APIView):
	"""docstring for SnippetDetail"""
	#permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
	def get_object(self, pk):
		try:
			return TestModel.objects.get(pk=pk)
		except TestModel.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		message 	= self.get_object(pk)
		serializer 	= TestSerializer(message)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		message = self.get_object(pk)
		serializer = TestSerializer(message, data=request.DATA)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		message 	= self.get_object(pk)
		message.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
