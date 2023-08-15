from dataclasses import dataclass

import pygame

import signals
from editor.editor import Editor


@dataclass
class EventPackage:
    """Convenient packaging for events"""

    events: list[pygame.event.Event]
    dt: float


class Core:
    """The core of all operations"""

    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((1100, 650), pygame.SCALED)
        self.clock = pygame.time.Clock()
        self.editor = Editor()

    def _update(self):
        events = pygame.event.get()
        dt = self.clock.tick() / 1000

        for event in events:
            if event.type == pygame.QUIT:
                raise SystemExit

        event_package = EventPackage(events, dt)
        signals.send("ep", event_package)
        self.editor.update()
        pygame.display.update()

    def _draw(self):
        self.screen.fill((180, 180, 180))

    def run(self):
        while True:
            self._update()
            self._draw()


if __name__ == "__main__":
    core = Core()
    core.run()
