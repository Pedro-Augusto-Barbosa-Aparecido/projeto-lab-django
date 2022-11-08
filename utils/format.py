from functools import partial
from operator import is_not

from .generics.formatter import Formatter
from .exceptions.not_found import NotFoundKeyOnList


class FormatDictQuery(Formatter):
    def format_for_create(self, query: dict, keys_to_search: list[str]):
        keys = ','.join(list(query.keys()))
        values = ','.join(map(lambda value: f'"{value}"',
                              filter(partial(is_not, None), map(lambda key: query.get(key, None), keys_to_search))))

        return {"keys": keys, "values": values}

    def format_for_list_or_get(self, query: dict, keys_to_search: list[str]):
        keys = list(query.keys())
        for key in keys_to_search:
            try:
                index_insert = keys.index(key, 0)
            except ValueError as e:
                continue
            value_to_insert = query.get(key, None)
            if value_to_insert:
                keys.insert(index_insert, str(value_to_insert))

        return keys
