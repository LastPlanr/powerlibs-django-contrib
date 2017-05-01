# Powerlibs Django Contrib

Some contributions to facilitate construction of Django projects

## Installation

```bash
$ pip install 'git+https://github.com/DroneMapp/powerlibs-django-contrib.git'
```

## Models Mixins

### OwnedModelMixin

Adds a `created_by` field to your model.

```python
from powerlibs.django.contrib.models import OwnedModelMixin


class MyModel(OwnedModelMixin):
    pass
```

### TimestampedModelMixin

Adds a `created_at` and a `updated_at` fields to your model.

```python
from powerlibs.django.contrib.models import TimestampedModelMixin


class MyModel(TimestampedModelMixin):
    pass
```

### TimestampedOwnedModelMixin

It just inherits both from OwnedModelMixin and TimestampedModelMixin (that
is: it will add `created_by`, `created_at` and `updated_at` to your
model).

```python
from powerlibs.django.contrib.models import TimestampedModelMixin


class MyModel(TimestampedModelMixin):
    pass
```

### SoftDeletableModelMixin

It adds a `deleted` field to your model, but **does not** change the
behavior of the `delete` method.

```python
from powerlibs.django.contrib.models import SoftDeletableModelMixin


class MyModel(SoftDeletableModelMixin):
    pass
```

## Admin Mixins

### CreatedByAdminMixin

When saving a model through `contrib.admin` site, doesn't show
`created_by` in the form and auto-fill it with the current logged user.


```python
from django.contrib import admin
from powerlibs.django.contrib.admin import CreatedByAdminMixin

from .models import MyModel

class MyModelAdmin(CreatedByAdminMixin, admin.ModelAdmin):
    pass

admin.site.register(MyModel, MyModelAdmin)
```
