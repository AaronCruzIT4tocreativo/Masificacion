from dataclasses import dataclass, field
from sender_instance import SenderInstance

@dataclass
class SenderInstancesService:
    instances: list = field(default_factory=list)

    def append_instance (self, sender_instance: SenderInstance):
        self.instances.append(sender_instance)

    def play_instance(self, index: int):
        self.instances[index].play()

    def pause_instance(self, index: int):
        self.instances[index].pause()

    def stop_instance(self, index: int):
        self.instances[index].stop()

    def set_instance_queue(self, index: int, values: list):
        self.instances[index].set_sender_queue(values)
