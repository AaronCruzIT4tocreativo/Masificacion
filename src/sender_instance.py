from dataclasses import dataclass, field
from sender import Sender
from threading import Event, Thread

@dataclass
class SenderInstance:
    sender: Sender = field(default_factory=Sender)
    play_event: Event = field(default_factory=Event)
    is_running: bool = field(default=False)
    play_thread: Thread = field(init=False)

    def __post_init__(self):
        self.play_thread = Thread(target=self.on_play)
        self.play_thread.start()

    def play(self):
        self.is_running = True
        self.play_event.set()

    def on_play(self):
        self.play_event.wait()
        self.play_event.clear()
        if self.is_running:
            self.sender.send_values(self.is_running)
            self.on_play()

    def pause(self):
        self.play_event.clear()

    def stop(self):
        self.is_running = False
        self.sender.queue.clear()

    def set_up(self, values: list):
        self.sender.queue.clear()
        self.sender.queue.extend(values)
        self.is_running = True
        self.play_event.set()
