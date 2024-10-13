from dataclasses import dataclass, field

@dataclass
class CustomDriver:
    element_names: list = field(default_factory=list)
    values: list = field(default_factory=list)

    def find_input_element(self, element: str):
        if element in self.element_names: 
            return "Element found"
        else:
            return "The input element is not found"