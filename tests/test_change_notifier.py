import json

import pytest


pytestmark = pytest.mark.django_db


def test_ChangeNotifierModel_status_change(mocked_notifier, change_notifier_model):
    # Create:
    instance = change_notifier_model(name='test 01')
    instance.save()

    assert mocked_notifier.notify.call_count == 1

    # Update:
    old_value = instance.status
    instance.status = 'status 2'
    instance.save()

    assert instance.debug_info['pre_creation_handler_called'] == 1
    assert instance.debug_info['post_creation_handler_called'] == 1
    assert instance.debug_info['pre_update_handler_called'] == 1
    assert instance.debug_info['post_update_handler_called'] == 1
    assert instance.debug_info['pre_delete_handler_called'] == 0
    assert instance.debug_info['post_delete_handler_called'] == 0

    assert mocked_notifier.notify.call_count == 2

    args, kwargs = mocked_notifier.notify.call_args
    message = json.loads(kwargs['Message'])
    data = json.loads(message['default'])

    assert kwargs['TopicArn'] == 'arn:test_create_topic:change_notifier_model__status_2'
    assert data['id'] == instance.pk
    assert data['_old_value'] == old_value


def test_ChangeNotifierModel_activation_change(mocked_notifier, change_notifier_model):
    # Create:
    instance = change_notifier_model(name='test changing activation data')
    instance.save()

    assert mocked_notifier.notify.call_count == 3

    # Update:
    old_value = instance.activated
    instance.activated = True
    instance.save()

    assert mocked_notifier.notify.call_count == 4

    args, kwargs = mocked_notifier.call_args
    message = json.loads(kwargs['Message'])
    data = json.loads(message['default'])

    assert kwargs['TopicArn'] == 'arn:test_create_topic:change_notifier_model__activated__true'
    assert data['id'] == instance.pk
    assert data['_old_value'] == old_value


def test_change_notifier_with_blank_value(mocked_notifier, change_notifier_model):
    blank_instance = change_notifier_model(name='', status='')
    blank_instance.save()

    topics = tuple(call[1]['TopicArn'].split(':')[-1] for call in mocked_notifier.call_args_list)
    assert 'change_notifier_model__blank' in topics

    """
    (
        'change_notifier_model__activated__false',
        'change_notifier_model__status_2',
        'change_notifier_model__activated__false',
        'change_notifier_model__activated__true',
        'change_notifier_model__blank',  # blank_instance.status
        'change_notifier_model__activated__false'   # blank_instance.activated
    )
    """
    assert mocked_notifier.notify.call_count == 6
