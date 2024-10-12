from dataclasses import dataclass, field
from collections import deque
import csv
from typing import Dict

@dataclass
class Sender:
    name: str
    queue: deque = field(default_factory=deque)

    def add_to_queue(self, values: list):
        self.queue.extend(values)

    def createCSV(self):
        filename = f"{self.name}.csv"
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['contact', 'message']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            while self.queue:
                item = self.queue.popleft()
                writer.writerow(item)
