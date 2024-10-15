import pytest
from sender_instance import SenderInstance
from sender import Sender

@pytest.fixture
def sender_instance(sender):
    si = SenderInstance(sender = sender)
    yield si
    si.is_running = False
    si.play_event.set()
    si.play_event.clear()
    si.play_thread.join()

@pytest.fixture
def sender():
    s = Sender(name="Instancia 0")
    values = [
        ["654", "hola"],
        ["123", "adios"]
    ]
    s.add_values_to_queue(values)
    return s

def test_play(sender_instance):
    sender_instance.play()
    assert sender_instance.is_running == True
    assert sender_instance.play_event.is_set() == True

def test_pause(sender_instance):
    sender_instance.pause()
    assert sender_instance.is_running == False
    assert sender_instance.play_event.is_set() == False

def test_stop(sender_instance, sender):
    sender_instance.stop()
    assert len(sender.queue) == 0
    assert sender_instance.is_running == False
    assert sender_instance.play_event.is_set() == False

def test_restart(sender_instance, sender):
    values = [
        ["997", "Hi from 997"],
        ["998", "Hi from 998"],
        ["999", "Hi from 999"]
    ]
    sender_instance.restart(values)
    assert sender_instance.is_running == True
    assert sender_instance.play_event.is_set() == True
    assert len(sender.queue) == 3
