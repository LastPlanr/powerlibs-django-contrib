from django.contrib.auth.models import User
from django.db import models


class OwnedModelMixin(models.Model):
    created_by = models.ForeignKey(User)

    class Meta:
        abstract = True


class TimestampedOwnedModelMixin(OwnedModelMixin):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
