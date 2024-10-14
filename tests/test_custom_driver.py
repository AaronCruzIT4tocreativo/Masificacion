import pytest
import asyncio
import asyncio
from custom_driver import CustomDriver

@pytest.fixture
def custom_driver():
    cd = CustomDriver()
    cd.input_elements_names = ["input0", "input1", "input2"]
    cd.inputs_values = ["value0", "value1", "value2"]
    return cd

def test_find_input_element(custom_driver):
    expected_input = "input0"
    result = custom_driver.find_input_element(expected_input)
    assert result == "Element found"
    
    expected_input = "input7"
    result = custom_driver.find_input_element(expected_input)
    assert result == {"status": "error", "message": "The input element is not found"}

def test_send_inputs_values(custom_driver):
    expected_result = {"status": "error", "message": "Missing Values"}
    result = custom_driver.send_inputs_values()
    assert expected_result == result

    expected_result = {"status": "ok", "message": "Message has been sent"}
    result = custom_driver.send_inputs_values(["value99", "value98", "value99"])
    assert expected_result == result
    assert custom_driver.inputs_values == ["value99", "value98", "value99"]
