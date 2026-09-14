from abc import ABC, abstractmethod


class Sound(ABC):
    @abstractmethod
    def read_aud(self) -> None:
        pass


class Video(ABC):
    @abstractmethod
    def read_vid(self) -> None:
        pass


class ProfCamera(Video):
    def read_vid(self) -> None:
        pass


class WebCamera(Video):
    def read_vid(self) -> None:
        pass


class ProfMicro(Sound):
    def read_aud(self) -> None:
        pass


class IntegratedMicro(Sound):
    def read_aud(self):
        pass
