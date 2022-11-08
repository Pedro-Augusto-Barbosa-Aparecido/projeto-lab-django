from abc import ABC, abstractmethod


class Formatter(ABC):
    @abstractmethod
    def format_for_create(self, query: dict, keys_to_search: list[str]):
        pass

    @abstractmethod
    def format_for_list_or_get(self, query: dict, keys_to_search: list[str]):
        pass
