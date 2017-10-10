from django.db import models
from django.db.models.deletion import Collector
from django.http import HttpResponse
from powerlibs.django.restless.modelviews import DetailEndpoint
from powerlibs.django.restless.http import Http400
from django.views.generic import View


def related_objects(target):
        collector = Collector(None)
        collector.add([target])

        yield from collector.instances_with_model()


class RelatedObjectsModelMixin(View, models.Model):
        """
        To use it this mixin, make a http OPTIONS request to the location you want to analyze.
        """

        class Meta:
            abstract = True

        allowed_methods = ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS']

        def options(self, request, *args, **kwargs):
            if 'OPTIONS' not in self.allowed_methods:
                return Http400('Method Not Allowed')

            related = []
            for model, obj in related_objects(DetailEndpoint.get_instance(self, request, *args, **kwargs)):
                related.append(obj)
                related.append(model)

            response = HttpResponse()
            response['Allow'] = self.allowed_methods
            response['Related-Objects'] = related

            return response
