from collections import deque
from dataclasses import dataclass, field
from sender import Sender
from threading import Event, Thread

@dataclass
class SenderInstance:
    sender: Sender = field(default_factory=Sender)
    play_event: Event = field(default_factory=Event)
    is_running: bool = field(default=False)
    play_thread: Thread = field(init=False)
    async_instructions: deque = field(init=False)

    def __post_init__(self):
        self.play_thread = Thread(target=self.on_play)
        self.play_thread.start()

    def play(self, service_queue: deque = deque()):
        self.async_instructions = service_queue
        self.is_running = True
        self.play_event.set()

    def on_play(self):
        self.play_event.wait()
        self.play_event.clear()
        if self.is_running:
            self.async_instructions.append(self.sender.send_case_values())
            self.on_play()

    def pause(self):
        self.play_event.clear()

    def stop(self):
        self.is_running = False
        self.sender.queue.clear()

    def set_sender_queue(self, values: list):
        self.sender.queue.clear()
        self.sender.queue.extend(values)
