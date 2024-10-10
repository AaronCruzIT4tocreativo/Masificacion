import pytest
import os
import csv
from sender import Sender

@pytest.fixture
def sender():
    name = "Test Sender"
    queue = [
        {"contact": "654", "message": "hola"},
        {"contact": "123", "message": "adios"}
    ]
    return Sender(name, queue)

def test_constructor(sender):
    assert sender.name == "Test Sender"
    assert sender.queue == [
        {"contact": "654", "message": "hola"},
        {"contact": "123", "message": "adios"}
    ]

def test_createCSV(sender):
    sender.createCSV()
    filename = f"{sender.name}.csv"
    
    assert os.path.exists(filename)
    
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        
    assert len(rows) == len(sender.queue)
    for i, row in enumerate(rows):
        assert row['contact'] == sender.queue[i]['contact']
        assert row['message'] == sender.queue[i]['message']
    
    os.remove(filename)
    