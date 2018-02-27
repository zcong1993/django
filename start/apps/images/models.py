from django.db import models
from django.utils.translation import ugettext_lazy as _

from start.apps.common.models import BaseModel, SoftDeleteModel
from .constants import Gender

# Create your models here.
class Image(BaseModel, SoftDeleteModel):
    user_id = models.IntegerField(verbose_name=_("UserId"))
    name = models.CharField(max_length=255, verbose_name=_("image name"))
    url = models.CharField(max_length=255, verbose_name=_("image url"))
    gender = models.IntegerField(verbose_name="Gender", default=Gender.MALE, choices=Gender.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("image")
        db_table = "image"
        verbose_name_plural = _("images")
