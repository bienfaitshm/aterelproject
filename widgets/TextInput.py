import customtkinter as ctk
import tkcalendar as tkc
import tkinter as tk
from typing import Optional, Any, Protocol
from .BaseFrame import BaseFrame


class FieldState(Protocol):
    value: tk.Variable
    texterror: tk.StringVar


class EntryBase(BaseFrame):
    def __init__(
        self,
        master: Any,
        label: str,
        fieldstate: Optional[FieldState] = None,
        placeholder: Optional[str] = None,
        *args, **kwargs
    ):
        super().__init__(master=master, *args, **kwargs)
        self.columnconfigure(0, weight=1)
        self.fieldstate = fieldstate

        self.label_text = ctk.CTkLabel(
            master=self, text=label)
        self.label_text.grid(row=0, column=0, sticky="w")

        self.text_error = ctk.CTkLabel(
            self, text="champ requis", textvariable=self.texterror, text_color="red", font=("", 10, "normal"))
        self.text_error.grid(row=2, column=0, sticky="w")

    @property
    def value(self, ) -> Optional[tk.Variable]:
        if self.fieldstate:
            return self.fieldstate.value

    @property
    def texterror(self) -> Optional[tk.Variable]:
        if self.fieldstate:
            return self.fieldstate.texterror


class TextInput(EntryBase):
    def __init__(self, master: Any, label: str, fieldstate: Optional[FieldState] = None, placeholder: Optional[str] = None, *args, **kwargs):
        super().__init__(master, label, fieldstate, placeholder, *args, **kwargs)
        self.text_entry = ctk.CTkEntry(
            master=self,
            placeholder_text=placeholder,
            border_width=1,
            corner_radius=2,
            width=300,
            textvariable=self.value,
            height=30,
        )
        self.text_entry.grid(row=1, column=0, sticky="ew")


class DateEntry(EntryBase):
    def __init__(self, master: Any, label: str, fieldstate: Optional[FieldState] = None, placeholder: Optional[str] = None, *args, **kwargs):
        super().__init__(master, label, fieldstate, placeholder, *args, **kwargs)
        self.text_entry = tkc.DateEntry(
            master=self,
            placeholder_text=placeholder,
            border_width=1,
            corner_radius=2,
            textvariable=self.value,
            height=40,
        )
        self.text_entry.grid(row=1, column=0, sticky="ew")
