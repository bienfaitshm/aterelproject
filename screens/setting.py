import os
import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog
from typing import Optional, Union, Any, Tuple, Callable, Dict
from widgets.BaseFrame import BaseFrame
from widgets.Button import Button


class SettingState:
    def __init__(self, presenter) -> None:
        self.theme = tk.StringVar(value=presenter.config.theme)
        self.path = tk.StringVar(value=presenter.config.docfolder)

    def initialize(self, *args, **kwargs) -> None:
        for key in kwargs:
            if hasattr(self, key):
                attribute: tk.Variable = getattr(self, key)

    def set(self, name: str, value: Any):
        if hasattr(self, name) and hasattr(getattr(self, name), "set"):
            getattr(self, name).set(value)


class SettingItem(BaseFrame):
    def __init__(self, parent, actions: Callable[[Any], ctk.CTkBaseClass], title: str = "header", subtitle: str = "subtitle", headerprops: Dict[str, Any] = None, subtitleprops: Dict[str, Any] = None, fg_color=None, corner_radius=20, height=70, width=600, *args, **kwargs):
        if headerprops is None:
            headerprops = {}
        if subtitleprops is None:
            subtitleprops = {}
        super().__init__(parent, corner_radius=corner_radius,
                         width=width, height=height, fg_color=fg_color, *args, **kwargs)

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=4)
        self.columnconfigure(1, weight=1)
        self.grid_propagate(False)

        # text container
        self.textcontainer = BaseFrame(self,)
        self.textcontainer.grid(row=0, column=0, sticky="nsew")

        # actioncontainer
        self.actioncontainer = BaseFrame(self,)
        self.actioncontainer.grid(row=0, column=1, sticky="nsew")

        # header
        self.header = ctk.CTkLabel(
            self.textcontainer, text=title, font=("", 14, "bold"), anchor=tk.W, bg_color="transparent", fg_color="transparent", **headerprops)
        self.header.grid(
            row=0, column=0, sticky=tk.W, pady=(10, 0), padx=(10, 0))

        # subtitle
        self.subtitle = ctk.CTkLabel(
            self.textcontainer, text=subtitle, text_color="gray60", font=("", 10, "bold"), bg_color="transparent", **subtitleprops)
        self.subtitle.grid(
            row=1, column=0, sticky=tk.W, pady=(0, 10), padx=(10, 0))

        # actions
        self.action = actions(self.actioncontainer)
        self.action.pack(fill=tk.BOTH, expand=tk.YES)


class SettingScreen(BaseFrame):

    def __init__(self, master: Union[tk.Tk, tk.Frame], presenter, *args, **kwargs):
        super().__init__(master=master, *args, **kwargs)

        # settings state
        self.state = SettingState(presenter=presenter)
        self.presenter = presenter

        # items container
        self.container = BaseFrame(self, width=500)
        self.container.pack()

        # text header setting

        self.ltitle = ctk.CTkLabel(
            self.container, text="Parametres", font=("", 20, "bold"))
        self.ltitle.grid(row=0, column=0, padx=20, pady=30, sticky=tk.W)

        # theme
        self.theme = SettingItem(
            self.container,
            title="Theme",
            subtitle="lorem.....",
            actions=lambda parent: ctk.CTkOptionMenu(
                parent, values=["system", "dark", "light"], command=self.change_mode
            ),
            subtitleprops={
                "textvariable": self.state.theme
            }
        )
        self.theme.grid(row=1, column=0, padx=5, pady=5)

        # folder
        self.folderpicker = SettingItem(
            self.container, actions=lambda parent: Button(
                parent, command=self.change_folder, text="Choisir", height=40, width=40
            ),
            title="Folder to save document",
            subtitleprops={
                "textvariable": self.state.path
            }
        )

        self.folderpicker.grid(row=2, column=0, padx=5, pady=5)

    def change_mode(self, mode):
        ctk.set_appearance_mode(mode)
        self.state.set("theme", mode)
        self.presenter.config.set_config("theme", mode)

    def change_folder(self):
        if directory := filedialog.askdirectory(initialdir=self.state.path.get()):
            self.state.set("path", directory)
            self.presenter.config.set_config("folder", directory)
