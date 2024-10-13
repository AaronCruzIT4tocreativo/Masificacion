import pytest
from custom_driver import CustomDriver

@pytest.fixture
def custom_driver():
    cd = CustomDriver()
    cd.input_element_names = ["input0", "input1", "input2"]
    cd.input_values = ["value0", "value1", "value2"]
    return cd

def test_find_input_element(custom_driver):
    expected_input = "input0"
    result = custom_driver.find_input_element(expected_input)
    assert result == "Element found"
    
    expected_input = "input7"
    result = custom_driver.find_input_element(expected_input)
    assert result == "The input element is not found"
