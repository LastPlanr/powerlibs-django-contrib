from django.db.models.deletion import Collector


def related_objects(target):
    collector = Collector(None)
    collector.add([target])

    yield from collector.instances_with_model()
