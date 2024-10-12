from dataclasses import dataclass, field

@dataclass
class CustomDriver:
    elements: list = field(default_factory=list)
    values: list = field(default_factory=list)

    def set_input_elements(self, elements: list):
        self.elements = elements

    def set_input_values(self, values: list):
        self.values = values

    def find_input_element(self, element: str):
        if element not in self.elements: 
            return "The input element is not found"
