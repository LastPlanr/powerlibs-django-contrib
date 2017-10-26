from django.db.models.deletion import Collector
from django.http import HttpResponse
from powerlibs.django.restless.modelviews import DetailEndpoint
from powerlibs.django.restless.http import Http400


class RelatedObjectsMixin(DetailEndpoint):
    """
    To use it this mixin, make an http OPTIONS request
    to the location you want to analyze.
    """
    def options(self, request, *args, **kwargs):
        if 'OPTIONS' not in self.allowed_methods:
            return Http400('Method Not Allowed')

        instance = self.get_instance(request, *args, **kwargs)

        response = HttpResponse(self.related_objects(instance))

        response['Allow'] = self.allowed_methods

        return response

    def related_objects(target):
        collector = Collector(None)
        collector.add([target])

        yield from collector.instances_with_model()
