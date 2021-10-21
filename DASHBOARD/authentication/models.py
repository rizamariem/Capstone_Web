# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models

# Create your models here.
class User(models.Model):
	username = models.CharField(max_length = 100)
	email = models.CharField(max_length = 100)
	password = models.CharField(max_length = 100)

	class Meta:
		db_table = "user"