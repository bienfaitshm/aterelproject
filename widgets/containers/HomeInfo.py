import tkinter as tk
import customtkinter as ctk
from typing import Any, Optional, Callable, Tuple, List

from widgets.BaseFrame import BaseFrame
from widgets.Button import Button
from widgets.Image import Image


class Card(BaseFrame):
    def __init__(self, master, title, sublabelprops: Optional[dict[str, Any]] = None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        if sublabelprops is None:
            sublabelprops = {}

        self.title = ctk.CTkLabel(
            self, text=title, fg_color="transparent", anchor=tk.W, font=("", 14, "bold"))
        self.title.grid(row=0, column=0, padx=10, pady=(5, 0), sticky=tk.W)

        self.subtext = ctk.CTkLabel(
            self, text="unknow", font=("", 12, "normal"), fg_color="transparent", anchor=tk.W, **sublabelprops)
        self.subtext.grid(row=1, column=0, padx=10, pady=(0, 2),  sticky=tk.W)


class CardTitle(BaseFrame):
    def __init__(self, master, title: str, items: Optional[List[Tuple[str, Optional[dict]]]] = None, *args, **kwargs):
        if items is None:
            items = []
        super().__init__(master, *args, **kwargs)

        self.title = ctk.CTkLabel(
            self, text=title.upper(), font=("", 14, "normal"))
        self.title.grid(row=0, column=0, sticky="w", padx=(5, 0))

        for iid, props in enumerate(items):
            # self.grid_columnconfigure(iid, weight=1)
            itemtitle, itemprops = props
            Card(self, title=itemtitle, sublabelprops=itemprops, fg_color=None, corner_radius=5).grid(
                row=1 + iid, column=0, sticky="we", padx=5)


class InfoFrame(BaseFrame):

    def __init__(self, parent: tk.Frame, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # variables
        self.name = tk.StringVar()
        self.adress = tk.StringVar()
        self.email = tk.StringVar()
        self.m_total = tk.IntVar()
        self.m_payer = tk.IntVar()
        self.m_rest = tk.IntVar()
        #

        self.headertext = ctk.CTkLabel(
            self, text="Impression", font=("", 16, "normal"))
        self.headertext.grid(row=0, column=0,)

        self.container = BaseFrame(self)
        self.container.grid_columnconfigure(0, weight=1)
        self.container.grid(row=1, column=0, sticky="nswe")

        CardTitle(
            self.container,
            title="Client",
            items=[
                ("Nom", {"textvariable": self.name}),
                ("Adresse", {"textvariable": self.adress}),
                ("Email / Tel", {"textvariable": self.email})
            ]
        ).grid(row=0, column=0, sticky="we", pady=5)

        CardTitle(
            self.container,
            title="Versements",
            items=[
                ("Total", {"textvariable": self.m_total}),
                ("Payer", {"textvariable": self.m_payer}),
                ("Restes", {"textvariable": self.m_rest})
            ]
        ).grid(row=2, column=0, sticky="we", pady=5)

    def setdata(self, *args, **kwargs):
        for key in kwargs:
            if hasattr(self, key):
                item = getattr(self, key)
                if hasattr(item, "set"):
                    item.set(kwargs.get(key))


class HomeInfo(BaseFrame):
    def __init__(
        self,
        master: Any,
        closeinfo: Optional[Callable[[], None]] = None,
        onsave: Optional[Callable[[], None]] = None,
        onsaveprint: Optional[Callable[[], None]] = None,
        *args, **kwargs
    ) -> None:
        super().__init__(master, *args, **kwargs)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self.closeinfo = closeinfo
        self.item = tk.Variable(self, value=None)
        self.onsave = onsave
        self.onsaveprint = onsaveprint

        # main

        self.container = BaseFrame(self, width=400)
        self.container.grid_columnconfigure(0, weight=1)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

        self.infosframe = InfoFrame(self.container)
        self.infosframe.grid(row=0, column=0, sticky="nsew")

        # btns
        self.savecontainer = BaseFrame(self.container)
        self.savecontainer.grid_columnconfigure(1, weight=1)
        self.savecontainer.grid(row=1, column=0, sticky="swe", pady=(0, 30))

        self.btnsave = Button(
            self.savecontainer, text="Enregistrer", command=self._onsave, corner_radius=20)
        self.btnsave.grid(row=0, column=0, sticky="we", padx=(0, 10))

        self.btnsaveprint = Button(
            self.savecontainer, text="Enregistrer et imprimer", command=self._onsaveprint, corner_radius=20)
        self.btnsaveprint.grid(row=0, column=1, sticky="ew", padx=(10, 0))

        # close container
        self.clscontainer = BaseFrame(
            self, width=60, height=60, bg_color="blue")
        self.clscontainer.grid_propagate(False)
        self.clscontainer.grid(row=0, column=0, sticky="ne", pady=10, padx=10)

        self.closebtn = Button(
            self.clscontainer,
            text=None,
            fg_color="transparent",
            corner_radius=5,
            height=60, width=60,
            command=self._closeinfo,
            image=Image(light_image="icons8-cancel-100.png", size=(25, 25))
        )
        self.closebtn.grid_propagate(False)
        self.closebtn.grid(row=0, column=0, sticky="nsew")

    def _closeinfo(self):
        if self.closeinfo is not None:
            self.closeinfo()

    def refrechitem(self, *args, **kwargs):
        self.infosframe.setdata(*args, **kwargs)
        print("refresh")

    def _onsave(self):
        if self.onsave:
            self.onsave()

    def _onsaveprint(self):
        if self.onsaveprint:
            self.onsaveprint()
