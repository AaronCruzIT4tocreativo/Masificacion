from collections import deque
import pytest
from sender_instances_service import SenderInstancesService
from sender_instance import SenderInstance
from sender import Sender

@pytest.fixture
def sender_instances_service(sender_instance):
    sis = SenderInstancesService()
    sis.instances.append(sender_instance)
    return sis

@pytest.fixture
def sender_instance(sender):    
    sis = SenderInstance(sender=sender)
    return sis

@pytest.fixture
def sender():
    s = Sender(name="Instancia 0")
    return s

def test_append_instance(sender_instances_service, sender_instance):
    sender_instances_service.append_instance(sender_instance)
    assert len(sender_instances_service.instances) == 2

def test_play_instance(sender_instances_service, sender_instance):
    sender_instances_service.play_instance(0)
    assert sender_instance.play_event.is_set == True

def test_pause_instance(sender_instances_service, sender_instance):
    sender_instances_service.pause_instance(0)
    assert sender_instance.play_event.is_set == False

def test_stop_instance(sender_instances_service, sender_instance):
    sender_instances_service.stop_instance(0)
    assert sender_instance.play_event.is_set == False

def test_set_instance_queue(sender_instances_service, sender):
    values = [
        ["654", "hola"],
        ["123", "adios"]
    ]
    sender_instances_service.set_instance_queue(deque(values))
    assert len(sender.queue) == 2
