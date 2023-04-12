import tkinter as tk
import customtkinter as ctk
from typing import Optional, Callable
from widgets.BaseFrame import BaseFrame
from widgets.Image import Image

RETURN_EVT = "<Return>"


class SearchInput(BaseFrame):
    def __init__(self,
                 parent,
                 onsubmit: Optional[Callable[[str], None]] = None,
                 fg_color=None, *args, **kwargs):
        super().__init__(parent, fg_color=fg_color, * args, **kwargs)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.grid_propagate(False)

        #
        # self.textvariable = tk.StringVar(self, value="Search...")
        self.onsubmit = onsubmit

        # root container
        self.container = BaseFrame(self)
        self.container.columnconfigure(0, weight=1)
        self.container.rowconfigure(0, weight=1)
        self.container.grid(
            row=0, column=0, padx=(25, 10), pady=2, sticky="nsew")

        self.input = ctk.CTkEntry(
            self.container, border_width=0, width=250, fg_color="transparent", placeholder_text="Search...")
        self.input.grid(row=0, column=0, sticky="wens", padx=(0, 10))
        self.input.bind(RETURN_EVT, self._onsubmit)

        self.btnsearch = ctk.CTkButton(
            self.container, command=self._onsubmit, image=Image(light_image="icons8-search-100.png"), text="", height=30, width=35, fg_color="transparent", corner_radius=5)
        self.btnsearch.grid(row=0, column=1,)
        self.btnsearch.grid_propagate(False)

    def _onsubmit(self, *args, **kwargs):
        """ submit handler"""
        if self.onsubmit:
            self.onsubmit(self.input.get())
