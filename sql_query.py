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
            "MIGRATION_PATH": [],
            "SQL_MIGRATION": [],
            "SQL_MIGRATION_PATH": []
        }

        for app_name in self._apps:
            for file_name in os.listdir(os.path.join(os.getcwd(), app_name, "migrations")):
                if not any(sub_string in file_name for sub_string in ["__init", "__pycache"]):
                    current_path = os.path.join(os.getcwd(), app_name, "migrations")
                    migration = self._get_migration_name(file_name)

                    migrations_dict["APP_NAME"].append(app_name)
                    migrations_dict["MIGRATION"].append(file_name)
                    migrations_dict["MIGRATION_NAME"].append(migration)
                    migrations_dict["MIGRATION_PATH"].append(current_path)

                    if not os.path.exists(f"{self.__default_output_path}\\{app_name}"):
                        os.mkdir(f"{self.__default_output_path}\\{app_name}")

                    os.system(
                        f"python manage.py sqlmigrate {app_name} {migration} > "
                        f"{self.__default_output_path}\\{app_name}\\{app_name}_{file_name.replace('.py', '')}.sql")

                    file = open(
                        f"{self.__default_output_path}\\{app_name}\\{app_name}_{file_name.replace('.py', '')}.sql",
                        'r',
                        encoding="utf-8"
                    )
                    migrations_dict["SQL_MIGRATION"].append(file.read().replace("[0m", ""))
                    migrations_dict["SQL_MIGRATION_PATH"].append(
                        f"{self.__default_output_path}\\{app_name}\\{app_name}_{file_name.replace('.py', '')}.sql")
                    file.close()

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
    from proj.settings import MY_APPS

    sql = SQLQuery(MY_APPS)
    sql.get_query_migrations()
