from dataclasses import dataclass, field

@dataclass
class SenderInstancesService:
    instances: list = field(default_factory=list)

    def play_instance(self, index: int):
        self.instances[index].play()