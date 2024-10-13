import pytest
import asyncio
from custom_driver import CustomDriver

@pytest.fixture
def custom_driver():
    cd = CustomDriver()
    cd.input_elements_names = ["input0", "input1", "input2"]
    cd.input_values = ["value0", "value1", "value2"]
    return cd

def test_find_input_element(custom_driver):
    expected_input = "input0"
    result = custom_driver.find_input_element(expected_input)
    assert result == "Element found"
    
    expected_input = "input7"
    result = custom_driver.find_input_element(expected_input)
    assert result == {"status": "error", "message": "The input element is not found"}

def test_send_inputs_values(custom_driver):

    async def delayed_input(delay, name):
        await asyncio.sleep(delay)
        return name

    custom_driver = CustomDriver()
    custom_driver.input_elements_names = [
        lambda: delayed_input(1, "input0"),
        lambda: delayed_input(1, "input1"),
        lambda: delayed_input(1, "input2")
    ]

    async def awaitInputs():
        resultados = await asyncio.gather(*(funcion() for funcion in custom_driver.input_elements_names))
        print(resultados)

    asyncio.run(awaitInputs())


    expected_result = {"status": "ok", "message": "Message has been sent"}
    result = custom_driver.send_inputs_values()
    assert expected_result == result
    assert custom_driver.inp
