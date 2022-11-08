from django.db import connection


class Connection:
    def __init__(self):
        self.__con = connection

    def list(self, query: str):
        row = []
        with self.__con.cursor() as cursor:
            cursor.execute(query)
            row = cursor.fetchall()

        return row
