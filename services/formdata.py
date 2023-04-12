from typing import Dict, Callable, Union, Literal
import tkinter as tk
from datetime import date

TYPE_FIELD = Union[Literal["string"], Literal["integer"], Literal["date"]]
RETURN_TYPE = Union[str, int, date]
DEFAULT_VALUE_FIELD_TYPE = Dict[str, Callable[[], RETURN_TYPE]]

DEFAULT_VALUE_FIELD: DEFAULT_VALUE_FIELD_TYPE = {
    "string": lambda: "",
    "integer": lambda: 0,
    "date": lambda: date.today(),
}


class Field:
    def __init__(self, typefield: TYPE_FIELD = "string", required: bool = False, *args, **kwargs) -> None:
        self.typefield: TYPE_FIELD = typefield
        self.required: bool = required


class StateField:
    error: bool = False

    def __init__(self, master: Union[tk.Misc, tk.Frame], field: Field) -> None:
        self.field = field
        self.texterror = tk.StringVar(master=master, value="")
        self.value = tk.Variable(
            master=master,
            value=self.get_defaulvalue(
                DEFAULT_VALUE_FIELD,
                typefield=self.field.typefield
            ))

    def get_defaulvalue(self, setupvalue: DEFAULT_VALUE_FIELD_TYPE, typefield: TYPE_FIELD = "string") -> RETURN_TYPE:
        return callback() if (callback := setupvalue.get(typefield)) else ""

    def is_valid(self) -> bool:
        value: RETURN_TYPE = self.value.get()
        if self.field.required and not str(value):
            self.texterror.set("Chant requis")
            self.error = True
        else:
            self.reset_error()
        return not self.error

    def reset(self) -> None:
        self.value.set(self.get_defaulvalue(
            DEFAULT_VALUE_FIELD, typefield=self.field.typefield))
        self.reset_error()

    def reset_error(self):
        self.texterror.set("")
        self.error = False


class DataFormState:
    fields: Dict[str, Field] = {
        # clients infos
        "name": Field(required=True),
        "adress": Field(required=True),
        "email": Field(required=True),
        "phone": Field(required=True),
        # produits infos
        "num_id": Field(required=True),
        "num_p_id": Field(required=True),
        "num_inpot": Field(required=True),
        "num_rccm": Field(required=True),
        # Versement
        "m_payer": Field(required=True, typefield="integer"),
        "m_total": Field(required=True, typefield="integer"),
        "m_rest": Field(required=True, typefield="integer"),
        "date": Field(required=True, typefield="date"),
    }

    def __init__(self, master) -> None:
        self.datas = self.create_state(master)

    def create_state(self, master) -> Dict[str, StateField]:
        return {
            fieldname: StateField(master, field=fieldoptions)
            for fieldname, fieldoptions in self.fields.items()
        }

    def is_valide(self) -> bool:
        valides: list[bool] = [
            field.is_valid() for field in self.datas.values()]
        return all(valides)

    def values(self) -> Dict[str, RETURN_TYPE]:
        """ parse value """
        return {
            key: field.value.get() for key, field in self.datas.items()
        }

    def reset(self) -> None:
        """ reset formulaire"""
        for field in self.datas.values():
            field.reset()

    def fieldstate(self, name: str) -> StateField | None:
        return self.datas.get(name)
