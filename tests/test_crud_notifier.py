import json

import pytest


pytestmark = pytest.mark.django_db


def test_CRUDNotifierModel_creation(mocked_notifier, crud_notifier_model):
    instance = crud_notifier_model(name='creation test')
    instance.save()

    assert mocked_notifier.notify.call_count == 1

    args, kwargs = mocked_notifier.notify.call_args
    message = json.loads(kwargs['Message'])
    data = json.loads(message['default'])

    assert kwargs['TopicArn'] == 'arn:test_create_topic:crud_notifier_model__created'
    assert data['id'] == instance.id
    assert data['name'] == 'creation test'


def test_CRUDNotifierModel_update(mocked_notifier, crud_notifier_model):
    instance = crud_notifier_model(name='creation test')
    instance.name = 'new name'
    instance.save()

    assert mocked_notifier.notify.call_count == 2  # For the UPDATE notification

    args, kwargs = mocked_notifier.notify.call_args
    message = json.loads(kwargs['Message'])
    data = json.loads(message['default'])

    assert kwargs['TopicArn'] == 'arn:test_create_topic:crud_notifier_model__updated'
    assert data['id'] == instance.id
    assert data['name'] == 'new name'


def test_CRUDNotifierModel_deletion(mocked_notifier, crud_notifier_model):
    instance = crud_notifier_model(name='creation test')
    instance.delete()
    assert mocked_notifier.notify.call_count == 3  # For the DELETE notification

    args, kwargs = mocked_notifier.notify.call_args
    message = json.loads(kwargs['Message'])
    data = json.loads(message['default'])

    assert kwargs['TopicArn'] == 'arn:test_create_topic:crud_notifier_model__deleted'
    assert data['id'] == instance.id
    assert data['name'] == 'new name'
