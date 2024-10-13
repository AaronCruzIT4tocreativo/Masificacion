from dataclasses import dataclass, field

@dataclass
class CustomDriver:
    input_elements_names: list = field(default_factory=list)
    values: list = field(default_factory=list)

    def find_input_element(self, element: str):
        if element in self.input_elements_names: 
            return "Element found"
        else:
            return {"status": "error", "message": "The input element is not found"}
