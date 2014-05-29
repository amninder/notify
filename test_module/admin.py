from django.contrib import admin
from test_module.models import TestModel

class TestAdmin(admin.ModelAdmin):
	"""docstring for TestAdmin"""
	list_diaplay	= ('message', 'title')
		
admin.site.register(TestModel, TestAdmin)