from dataclasses import dataclass, field
from collections import deque
import csv
from typing import Dict
from custom_driver import CustomDriver

@dataclass
class Sender:
    name: str
    custom_driver: CustomDriver
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
