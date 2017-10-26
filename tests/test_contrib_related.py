from unittest import mock

from powerlibs.django.contrib.related_objects import RelatedObjectsMixin


def test_related_objects(fake_request):
    request = fake_request()

    TestObject = mock.Mock(RelatedObjectsMixin, allowed_methods=['OPTIONS'])

    response = RelatedObjectsMixin.options(TestObject, request)

    assert response.status_code == 200, str(response.content, 'utf-8')
    assert 'OPTIONS' in response['Allow']
