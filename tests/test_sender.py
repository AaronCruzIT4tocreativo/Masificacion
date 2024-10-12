import pytest
import os
import csv
from collections import deque
from sender import Sender

@pytest.fixture
def sender():
    s = Sender(name="Test Sender")
    s.add_to_queue("654", "hola")
    s.add_to_queue("123", "adios")
    return s

def test_constructor(sender):
    assert sender.name == "Test Sender"
    assert isinstance(sender.queue, deque)
    assert len(sender.queue) == 2

def test_add_values_to_queue(sender):
    values = [
        {"contact": "997", "message": "Hi from 997"},
        {"contact": "998", "message": "Hi from 998"},
        {"contact": "999", "message": "Hi from 999"}
    ]

    sender.add_to_queue(values)
    assert len(sender.queue) == 5
    assert sender.queue[-1] == {"contact": "999", "message": "Hi from 999"}

def test_createCSV(sender):
    initial_queue_length = len(sender.queue)
    sender.createCSV()
    filename = f"{sender.name}.csv"
    
    assert os.path.exists(filename)
    assert len(sender.queue) == 0  # La cola debe estar vacía después de crear el CSV
    
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        
    assert len(rows) == initial_queue_length
    assert rows[0]['contact'] == "654"
    assert rows[0]['message'] == "hola"
    assert rows[1]['contact'] == "123"
    assert rows[1]['message'] == "adios"
    
    os.remove(filename)

def test_restart_queue(sender):
    values = [
        {"contact": "997", "message": "Hi from 997"},
        {"contact": "998", "message": "Hi from 998"},
        {"contact": "999", "message": "Hi from 999"}
    ]

    sender.restart_queue(values)
    assert len(sender.queue) == 3
