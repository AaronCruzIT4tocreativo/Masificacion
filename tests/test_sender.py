import asyncio
import pytest
import os
import csv
from collections import deque
from sender import Sender
from custom_driver import CustomDriver

@pytest.fixture
def custom_driver():
    cd = CustomDriver()
    cd.input_elements_names = ["input0", "input1", "input2"]
    cd.input_values = ["value0", "value1", "value2"]
    return cd

@pytest.fixture
def sender(custom_driver):
    s = Sender(name="Instancia 0", custom_driver=custom_driver)
    values = [
        ["654", "hola"],
        ["123", "adios"]
    ]
    s.add_values_to_queue(values)
    return s

def test_constructor(sender):
    assert isinstance(sender.queue, deque)
    assert len(sender.queue) == 2

def test_add_values_to_queue(sender):
    values = [
        ["997", "Hi from 997"],
        ["998", "Hi from 998"],
        ["999", "Hi from 999"]
    ]

    sender.add_values_to_queue(values)
    assert len(sender.queue) == 5
    assert sender.queue[-1] == ["999", "Hi from 999"]

def test_create_csv(sender):
    initial_queue_length = len(sender.queue)
    sender.create_csv()
    filename = f"{sender.name}.csv"
    
    assert os.path.exists(filename)
    assert len(sender.queue) == 0  # La cola debe estar vacía después de crear el CSV
    
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        rows = list(reader)
        
    assert len(rows) == initial_queue_length
    assert rows[0][0] == "654"
    assert rows[0][1] == "hola"
    assert rows[1][0] == "123"
    assert rows[1][1] == "adios"
    
    os.remove(filename)

def test_restart_queue(sender):
    values = [
        ["997", "Hi from 997"],
        ["998", "Hi from 998"],
        ["999", "Hi from 999"]
    ]

    sender.restart_queue(values)
    assert len(sender.queue) == 3

def test_send_values(sender):    
    assert sender.send_values(True) == {"status": "ok", "message": "Paused"}

    assert sender.send_values() == {"status": "ok", "message": "Messages Sent Successfully"}

    values = [
        ["997", "Hi from 997"],
        ["998", ""],
        ["999", "Hi from 999"]
    ]
    sender.queue = deque(values)
    assert sender.send_values() == {"status": "error", "message": "Empty Value"}

    sender.queue.clear()
    assert sender.send_values() == {"status": "error", "message": "Empty Queue"}

def test_set_inputs_names(custom_driver, sender):
    sender.set_inputs_names(["input7", "input9"])
    assert custom_driver.find_input_element("input7") == "Element found"
    assert custom_driver.find_input_element("input0") == {"status": "error", "message": "The input element is not found"}

def test_send_case_values(sender):
    assert asyncio.run((sender.send_case_values())()) == {"status": "ok", "message": "Async instructions haven been executed successfully"}
    assert len(sender.queue) == 1
    assert sender.queue.popleft() == ["123", "adios"]
