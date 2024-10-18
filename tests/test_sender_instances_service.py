import asyncio
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
    si = SenderInstance(sender=sender)
    yield si
    si.is_running = False
    si.play_event.set()
    si.play_event.clear()
    si.play_thread.join()

@pytest.fixture
def sender():
    s = Sender(name="Instancia 0")
    return s

def test_append_instance(sender_instances_service, sender_instance):
    sender_instances_service.append_instance(sender_instance)
    assert len(sender_instances_service.instances) == 2

def test_play_instance(sender_instances_service, sender_instance):
    async_instance_instructions = sender_instances_service.play_instance(0)
    assert asyncio.run(async_instance_instructions()) == {"status": "ok", "message": "Async instructions haven been executed successfully"}
    assert sender_instance.play_event.is_set() == True

def test_pause_instance(sender_instances_service, sender_instance):
    sender_instances_service.pause_instance(0)
    assert sender_instance.play_event.is_set() == False

def test_stop_instance(sender_instances_service, sender_instance):
    sender_instances_service.stop_instance(0)
    assert sender_instance.play_event.is_set() == False

def test_set_instance_queue(sender_instances_service, sender):
    values = [
        ["654", "hola"],
        ["123", "adios"]
    ]
    sender_instances_service.set_instance_queue(0, values)
    assert len(sender.queue) == 2

# def test_manage_async_instance_instructions(sender_instances_service):
#     sender_instances_service.manage_active_instance(0)
#     assert len(sender_instances_service.active_instances) == 1
#     assert asyncio.run(sender_instances_service.active_instances[0]()) == {"status"}
