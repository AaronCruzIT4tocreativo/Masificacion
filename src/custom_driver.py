from dataclasses import dataclass, field

@dataclass
class CustomDriver:
    input_elements_names: list = field(default_factory=list)
    inputs_values: list = field(default_factory=list)

    def find_input_element(self, element: str):
        if element in self.input_elements_names:
            return "Element found"
        else:
            return {"status": "error", "message": "The input element is not found"}

    def send_inputs_values(self, values: list = []):
        if len(values) == 0:
            return {"status": "error", "message": "Missing Values"}
        
        self.inputs_values = values

        for input_value in self.inputs_values:
            if input_value == "": return {"status": "error", "message": "Empty Value"}

        # Add the driver interaction logic here using the values
        
        return {"status": "ok", "message": "Message has been sent"}
