from collections import deque
from dataclasses import dataclass, field
from collections import deque
from sender_instance import SenderInstance

@dataclass
class SenderInstancesService:
    instances: list = field(default_factory=list)
    async_instances_instructions: deque = field(default_factory=deque)

    def append_instance (self, sender_instance: SenderInstance):
        self.instances.append(sender_instance)

    def play_instance(self, index: int):
        self.instances[index].play(main_queue=self.async_instances_instructions)

    def pause_instance(self, index: int):
        self.instances[index].pause()

    def stop_instance(self, index: int):
        self.instances[index].stop()

    def set_instance_queue(self, index: int, values: list):
        self.instances[index].set_sender_queue(values)
