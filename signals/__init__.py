class SignalManager:
    """
    Handles signal transactions

    Methods:
        - receive
        - send
    """

    def __init__(self) -> None:
        self.__queue = {}

    def receive(self, data_name: str, delete: bool = False) -> object:
        if delete:
            return self.__queue.pop(data_name)

        return self.__queue.get(data_name)

    def send(self, data_name: str, data: object) -> None:
        self.__queue[data_name] = data


signal_manager = SignalManager()


def receive(data_name: str, delete: bool = False) -> object:
    """Retrieves the data stored to a name and deletes it
    from memory.

    Parameters:
        data_name: The name of data to be received
        delete: Boolean to determine whether to delete
        the data after retrieving it or not.

    Returns:
        The data retrieved. None if data was not sent
    """

    return signal_manager.receive(data_name, delete)


def send(data_name: str, data: object) -> None:
    """Adds the data to be sent onto the queue. To be deleted
    after being received.

    Parameters:
        data_name: The name of data to be received
        data: The data to be sent
    """

    signal_manager.send(data_name, data)
