import pytest
from sender_instance import SenderInstance
from sender import Sender

@pytest.fixture
def sender_instance():
    si = SenderInstance()
    return si

@pytest.fixture
def sender():
    s = Sender()
    return s

def test_play(sender_instance):
    sender_instance.play()
    assert sender_instance.events.play.is_set() == True

def test_pause(sender_instance):
    sender_instance.pause()
    assert sender_instance.events.play.is_set() == False

def test_stop(sender_instance, sender):
    sender_instance.stop()
    assert sender_instance.events.play.is_set() == False
    assert len(sender.queue) == 0
    # assert sender_instance.events.stop.is_set() == False

def test_restart(sender_instance, sender):
    values = [
        []
    ]
    sender_instance.restart()
    assert sender_instance.events.play.is_set() == True
    assert len(sender.queue) == 0
    # assert sender_instance.events.restart.is_set() == False
