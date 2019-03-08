# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.encoding import python_2_unicode_compatible
from .Empresa import Empresa

@python_2_unicode_compatible
class User(AbstractUser):
    """ Modelo de usuario que reemplaza al modelo por default """
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT, verbose_name="Empresa", null=True)


    def __str__(self):
        return u"{0} {1}".format(self.first_name, self.last_name)


    def __unicode__(self):
        return u"{0} {1}".format(self.first_name, self.last_name)


    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'

