import os
import customtkinter as ctk
from typing import Optional, Tuple
from PIL import Image as PILImage
from settings import ICON_DIR


class Image(ctk.CTkImage):
    def __init__(self,
                 light_image: str,
                 dark_image: Optional[str] = None,
                 size: Tuple[int, int] = (25, 25)) -> None:
        dirname: str = ICON_DIR
        super().__init__(size=size,
                         light_image=self.get_image(dirname, light_image),
                         dark_image=self.get_image(
                             dirname, dark_image or light_image)
                         )

    def get_image(self, dirname: str, name: str) -> PILImage.Image:
        return PILImage.open(os.path.join(dirname, name))
