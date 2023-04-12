import tkinter as tk
import customtkinter as ctk


class Button(ctk.CTkButton):
    def __init__(self,
                 master,
                 height: int = 40,
                 corner_radius: int = 5,
                 border_width=0,
                 *args, **kwargs):
        super().__init__(master=master,
                         height=height,
                         corner_radius=corner_radius,
                         border_width=border_width,
                         *args, **kwargs)
