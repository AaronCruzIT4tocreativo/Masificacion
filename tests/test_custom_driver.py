import pytest
from custom_driver import CustomDriver

@pytest.fixture
def custom_driver():
    cd = CustomDriver()
    cd.set_input_elements(["input0", "input1", "input2"])
    cd.set_input_values(["value0", "value1", "value2"])
    return cd

def test_find_input_element(custom_driver):
    expected_input = "input3"
    result = custom_driver.find_input_element(expected_input)
    assert "The input element is not found" == result
