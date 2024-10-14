from dataclasses import dataclass, field
from sender import Sender
from threading import Event, Thread

@dataclass
class SenderInstance:
    sender: Sender = field(default_factory=Sender)
    play_event: Event = field(default_factory=Event)
    play_thread: Thread = field(init=False)

    def __post_init__(self):
        self.play_thread = Thread(target=self.on_play)
        self.play_thread.start()

    def play(self):
        self.play_event.set()

    def on_play(self):
        while True:
            self.play_event.wait()
            self.sender.send_values()
            self.play_event.clear()

    def pause(self):
        self.play_event.clear()
