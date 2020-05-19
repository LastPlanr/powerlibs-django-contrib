from django.db import models


class TimestampedModelMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SoftDeletableModelMixin(models.Model):
    deleted = models.BooleanField(default=False, editable=False)

    class Meta:
        abstract = True
