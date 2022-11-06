import os
import re

import pandas as pd
from colorama import Style, Fore, Back


class SQLQuery:
    def __init__(self, apps_name: list[str]):
        self._apps = apps_name
        self.__default_output_path = "./migrations_django"

    def get_query_migrations(self):
        if not os.path.exists(self.__default_output_path):
            os.mkdir(self.__default_output_path)

        print(
            Fore.GREEN + Style.BRIGHT + Back.BLACK +
            f"Scripts are saved on {re.sub(r'[.]', '', self.__default_output_path)}!" + Style.RESET_ALL)

        migrations_dict = {
            "APP_NAME": [],
            "MIGRATION": [],
            "MIGRATION_NAME": [],
            "MIGRATION_PATH": []
        }

        for app_name in self._apps:
            for file_name in os.listdir(os.path.join(os.getcwd(), app_name, "migrations")):
                if not any(sub_string in file_name for sub_string in ["__init", "__pycache"]):
                    migrations_dict["APP_NAME"].append(app_name)
                    migrations_dict["MIGRATION"].append(file_name)
                    migrations_dict["MIGRATION_NAME"].append(self._get_migration_name(file_name))
                    migrations_dict["MIGRATION_PATH"].append(os.path.join(".", app_name, "migrations"))

        migrations = pd.DataFrame.from_dict(migrations_dict)
        migrations.to_excel(f"{self.__default_output_path}\\migrations.xlsx", sheet_name="Migrations", index=False)

        print(
            Fore.MAGENTA + Style.BRIGHT + Back.BLACK +
            f"Saved migration info on {re.sub(r'[.]', '', self.__default_output_path)}/migrations.xlsx" +
            Style.RESET_ALL)

    @staticmethod
    def _get_migration_name(migration: str):
        return re.findall(r"^[0-9]{4}", migration)[0]


if __name__ == "__main__":
    sql = SQLQuery(['users', 'bases', 'bank'])
    sql.get_query_migrations()
