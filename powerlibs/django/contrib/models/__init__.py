from django.db import models


class TimestampedModelMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SoftDeletableModelMixin(models.Model):
    deleted = models.BooleanField(default=False, editable=False)

    def pre_delete_soft_deletable(self, **context):
        self._was_deleted = self.deleted

    def post_delete_soft_deletable(self, **context):
        previously_deleted = self._was_deleted

        if self.deleted and not previously_deleted:
            self.notify('deleted')
        elif previously_deleted and not self.deleted:
            self.notify('undeleted')

    class Meta:
        abstract = True
