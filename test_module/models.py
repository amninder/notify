from django.db import models

class TestModel(models.Model):
	message		= models.CharField(max_length=1000)
	def __unicode__(self):
		return self.message