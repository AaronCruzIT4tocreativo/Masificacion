from dataclasses import dataclass, field
from collections import deque
import csv
from typing import Dict
from custom_driver import CustomDriver

@dataclass
class Sender:
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

    def send_values(self):
        if len(self.queue) == 0:
            return {"status": "error", "message": "Empty Queue"}
        return {"status": "ok", "message": "Messages Sent Successfully"}
        
    def set_inputs_names(self, names: list):
        self.custom_driver.input_elements_names = names
