from django.db import models


class Register(models.Model):
	filename = models.CharField(max_length=100)
	docfile = models.FileField(upload_to='documents/%Y/%m/%d')

	def __str__(self):
		return self.filename