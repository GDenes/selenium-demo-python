from abc import abstractmethod


class DriverInterface:
    @abstractmethod
    def get_driver(self): raise NotImplementedError

    @abstractmethod
    def get_remote_driver(self, remoteUrl): raise NotImplementedError
