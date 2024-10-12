from dataclasses import dataclass, field

@dataclass
class CustomDriver:
    element_names: list = field(default_factory=list)
    values: list = field(default_factory=list)

    def set_input_element_names(self, element_names: list):
        self.element_names = element_names

    def set_input_values(self, values: list):
        self.values = values

    def find_input_element(self, element: str):
        if element not in self.element_names: 
            return "The input element is not found"
