from dataclasses import dataclass, field
import csv
from typing import List, Dict

@dataclass
class Sender:
    name: str
    queue: List[Dict[str, str]] = field(default_factory=list)

    def createCSV(self):
        filename = f"{self.name}.csv"
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['contact', 'message']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for item in self.queue:
                writer.writerow(item)
