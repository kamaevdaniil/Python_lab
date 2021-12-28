import os
import json


class Config:

    #  Загружает данные из файла конфига (только json)
    def load(self, file_path: str) -> None:
        file_extension = os.path.splitext(file_path)[1]

        if file_extension == '.json':
            with open(file_path, 'r') as f:
                config_data = json.load(f)
                for key, value in config_data.items():
                    setattr(self, key, value)

    #  Загружает данные из файла конфига
    def reload(self, file_path: str) -> None:
        for key in self.__dict__.copy().keys():  # пришлось создать копию словаря, иначе питон ругается
            delattr(self, key)
        self.load(file_path)

    #  Возвращает весь конфиг
    def get_all(self) -> dict:
        return self.__dict__