import os
from typing import Literal, Union
from services.utility import resource_path
BASE_DIRNAME = os.path.dirname(os.path.realpath(__file__))
# Theme config
APP_MODE_TYPE = Union[
    Literal["light"],
    Literal["dark"],
    Literal["system"]
]

APPARENCE_MODE: APP_MODE_TYPE = "dark"
COLOR_THEME: str = "green"

SIZE_APP: str = "768x564"
APP_NAME: str = "Aterell"


#
# os.path.join(BASE_DIRNAME, "assets/icons")
ICON_DIR = resource_path("assets/icons")
ASSETS_DIR = resource_path("assets/")  # os.path.join(BASE_DIRNAME, "assets/")
