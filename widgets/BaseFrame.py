import customtkinter as ctk
from typing import Optional, Union, Tuple, Any


class BaseFrame(ctk.CTkFrame):
    def __init__(self,
                 master: Any, width: int = 200, height: int = 200, corner_radius: Optional[Union[int, str]] = 0, border_width: Optional[Union[int, str]] = None, bg_color: Union[str, Tuple[str, str]] = "transparent", fg_color: Optional[Union[str, Tuple[str, str]]] = "transparent", border_color: Optional[Union[str, Tuple[str, str]]] = None, background_corner_colors: Union[Tuple[Union[str, Tuple[str, str]]], None] = None, overwrite_preferred_drawing_method: Union[str, None] = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color,
                         border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
