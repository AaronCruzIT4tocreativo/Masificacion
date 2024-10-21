import asyncio
from dataclasses import dataclass, field
from collections import deque
from threading import Thread, Event
import time
from sender_instance import SenderInstance

@dataclass
class SenderInstancesService:
    instances: list = field(default_factory=list)
    async_instances_instructions: deque = field(default_factory=deque)
    play_thread: Thread = field(init=False)
    play_event: Event = field(default_factory=Event)

    def __post_init__(self):
        self.play_thread = Thread(target=self.manage_async_instructions)
        self.play_thread.start()

    def append_instance (self):
        sender_instance = SenderInstance()
        self.instances.append(sender_instance)

    def play_instance(self, index: int):
        self.instances[index].play(main_queue=self.async_instances_instructions)

    def pause_instance(self, index: int):
        self.instances[index].pause()

    def stop_instance(self, index: int):
        self.instances[index].stop()

    def set_instance_queue(self, index: int, values: list):
        self.instances[index].set_sender_queue(values)
    
    def manage_async_instructions(self):
        while self.async_instances_instructions:
            instance_instructions = self.async_instances_instructions.popleft()
            asyncio.run(instance_instructions())
        time.sleep(1)
        if self.play_event.is_set(): self.manage_async_instructions()

    def stop_async_instructions(self):
        self.play_event.clear()
