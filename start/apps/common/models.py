# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now


# 自定义基类型:
class BaseModel(models.Model):
    created_at = models.DateTimeField(verbose_name=_("Created At"), auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=_("Updated At"), auto_now=True)

    class Meta:
        abstract = True


# 软删除:
class SoftDeleteModel(models.Model):
    # soft delete
    is_deleted = models.BooleanField(verbose_name=_("Api Is Deleted"), default=False)
    deleted_at = models.DateTimeField(verbose_name=_("Deleted At"), default=None, blank=True, null=True)

    def soft_delete(self):
        self.is_deleted = True
        self.deleted_at = now()
        self.save()

    class Meta:
        abstract = True
