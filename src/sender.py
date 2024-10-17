from dataclasses import dataclass, field
from collections import deque
import csv
from custom_driver import CustomDriver

@dataclass
class Sender:
    name: str
    custom_driver: CustomDriver = field(default_factory=CustomDriver)
    queue: deque = field(default_factory=deque)

    def add_values_to_queue(self, values: list):
        self.queue.extend(values)

    def create_csv(self):
        filename = f"{self.name}.csv"
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            
            while self.queue:
                item = self.queue.popleft()
                writer.writerow(item)

    def restart_queue(self, values: list):
        self.queue.clear()
        self.queue.extend(values)

    def send_values(self, pause: bool = False):
        if len(self.queue) == 0:
            return {"status": "error", "message": "Empty Queue"}
        while self.queue:
            if pause: return {"status": "ok", "message": "Paused"}
            values = self.queue.popleft()
            # Add Random Time Here
            result = self.custom_driver.send_inputs_values(values)
            if result != {"status": "ok", "message": "Message has been sent"}:
                return result
        return {"status": "ok", "message": "Messages Sent Successfully"}
        
    def set_inputs_names(self, names: list):
        self.custom_driver.input_elements_names = names

    def send_case_values(self):
        case_values = self.queue.popleft()
        self.custom_driver.send_inputs_values(case_values)
