import configparser
from services import utility
# import settings
import os
import sys
from settings import APPARENCE_MODE


DEFAULT = {
    "folder": utility.createdirdoc(),
    "theme": APPARENCE_MODE
}


class AppConfiguration:
    filename = "appconfig.ini"
    default = "DEFAULT"

    def __init__(self) -> None:
        self.config = configparser.ConfigParser()
        self.load_config()

    def load_config(self) -> None:
        if exist := os.path.exists(self.filename):
            self.read_config()
            return
        self.config[self.default] = DEFAULT
        self.write_config()

    def read_config(self) -> None:
        self.config.read(self.filename)

    def set_config(self, key, value) -> None:
        self.config[self.default][key] = value
        self.write_config()

    def write_config(self) -> None:
        with open(self.filename, 'w') as configfile:
            self.config.write(configfile)

    @property
    def docfolder(self) -> str:
        return self.config.get(self.default, "folder")

    @property
    def theme(self) -> str:
        return self.config.get(self.default, "theme")
