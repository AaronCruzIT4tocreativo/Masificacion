from dataclasses import dataclass, field
from sender import Sender

@dataclass
class SenderInstance:
    sender: Sender = field(default_factory=Sender)
