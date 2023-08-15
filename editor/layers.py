class Layer:
    """A Surface that can be used to place objects on.
    Has dynamic size based on objects placed"""


class LayerManager:
    """
    Handles all the layers. Decides in what order
    to draw them, what layers to show and their opacity
    """

    def __init__(self) -> None:
        self.layers: list[Layer] = []
