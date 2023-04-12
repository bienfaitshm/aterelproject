import tkinter as tk
from typing import TypedDict, Optional, Dict

ERROR_STATE = "error"
ERROR_TEXT_STATE = "text_error"
VALUE_STATE = "value"


ValueDict = Dict[str, tk.Variable]


class FormData(TypedDict):
    name: ValueDict
    adress: ValueDict
    phone: ValueDict
    email: ValueDict
    num_p_id: ValueDict
    num_id: ValueDict
    num_rccm: ValueDict
    num_inpot: ValueDict
    date: ValueDict
    m_total: ValueDict
    m_payer: ValueDict
    m_rest: Optional[ValueDict]


LIST_COLOMN = {
    "id": "ID",
    "name": "Nom",
    "adress": "Adresse",
    "phone": "Tel",
    "email": "Email",
    "num_p_id": "Id Num Produit",
    "num_rccm": "Num RCCM",
    "num_id": "Num ID",
    "num_inpot": "Num Impot",
    "m_total": "M. Total",
    "m_payer": "M. Payer",
    "m_rest": "M. Restant",
    "date": "Date"
}
