import pygame

import signals


class Editor:
    """Handles the operations related to the editor"""

    def __init__(self) -> None:
        pass

    def update(self):
        ep = signals.receive("ep")
        for event in ep.events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                print("DEBUG")
