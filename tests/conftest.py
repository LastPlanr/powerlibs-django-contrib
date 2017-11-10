import pytest


@pytest.fixture
def fake_request():
    user = type('object', (), {
        'id': 999,
        'is_authenticated': False,
    })

    r = type('object', (), {
        'GET': {'redirect-to': '/REDIRECT-TO/'},
        'user': user,
        'POST': {},
        'META': {},
        'session': {},
        'path': '/',
    })

    return r
