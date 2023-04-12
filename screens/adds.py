from datetime import datetime
import customtkinter as ctk
import tkinter as tk
from typing import Union
from widgets.TextInput import TextInput
from widgets.BaseFrame import BaseFrame
from widgets.Button import Button
from services.formdata import DataFormState

FORMAT_DATE = "%Y-%m-%d"


class InputTitleContainer(BaseFrame):
    def __init__(self, master: Union[tk.Misc, tk.Frame], title: str, column: int = 2, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        for i in range(column):
            self.columnconfigure(i, weight=1)

        self.title_label = ctk.CTkLabel(
            master=self, text=title, font=("", 12, 'bold'))
        self.title_label.grid(row=0, column=0, sticky="w", padx=5)


class FormContainer(BaseFrame):
    def __init__(self, master, state: DataFormState, *args, **kwargs):
        super().__init__(master=master, *args, **kwargs)
        self.state = state
        self.columnconfigure(0, weight=1)

        # Client INFO
        self.client_container = InputTitleContainer(
            master=self, title="CLIENT")
        self.client_container.grid()

        # Nom
        dom = TextInput(
            master=self.client_container,
            label="Nom",
            placeholder="Nom",
            fg_color="transparent",
            fieldstate=self.state.fieldstate("name")
        )
        dom.grid(row=1, column=0, sticky="nsew", padx=5)

        # Adress
        email = TextInput(
            master=self.client_container,
            label="Adresse",
            placeholder="Adresse",
            fieldstate=self.state.fieldstate("adress")
        )
        email.grid(row=1, column=1, sticky="nsew", padx=5)

        # Telephone
        tel = TextInput(
            master=self.client_container,
            label="Telephone",
            placeholder="Telephone",
            fieldstate=self.state.fieldstate("phone"),
        )
        tel.grid(row=2, column=0, sticky="nsew", padx=5)

        # Email
        email = TextInput(
            master=self.client_container,
            label="Email",
            placeholder="Email",
            fieldstate=self.state.fieldstate("email"))
        email.grid(row=2, column=1, sticky="nsew", padx=5)

        # Produit info
        self.produit_container = InputTitleContainer(
            master=self, title="PRODUIT")
        self.produit_container.grid(pady=5)

        # Numero pièce id
        num_p_id = TextInput(
            master=self.produit_container,
            label="Numero pièce id",
            placeholder="Numero pièce id",
            fieldstate=self.state.fieldstate("num_p_id"))
        num_p_id.grid(row=1, column=0, sticky="nsew", padx=5)

        # Numero RCCM
        num_rccm = TextInput(
            master=self.produit_container,
            label="Numero RCCM",
            placeholder="Numero RCCM",
            fieldstate=self.state.fieldstate("num_rccm")
        )
        num_rccm.grid(row=1, column=1, sticky="nsew", padx=5)

        # Numero id
        num_id = TextInput(
            master=self.produit_container,
            label="Numero id",
            placeholder="Numero id",
            fieldstate=self.state.fieldstate("num_id")
        )
        num_id.grid(row=2, column=0, sticky="nsew", padx=5)

        # Numero impot
        num_inpot = TextInput(
            master=self.produit_container,
            label="Numero impot",
            placeholder="Numero impot",
            fieldstate=self.state.fieldstate("num_inpot")
        )
        num_inpot.grid(row=2, column=1, sticky="nsew", padx=5)

        # time frame container
        self.vesersement_container = InputTitleContainer(
            master=self, title="VERSEMENT")
        self.vesersement_container.grid()

        # Title
        t_label = ctk.CTkLabel(master=self.vesersement_container, text="VERSEMENT", font=(
            "Helvetica bold", 12, 'bold'))
        t_label.grid(row=0, column=0, sticky="w", padx=5)

        # m_total
        m_total = TextInput(
            master=self.vesersement_container,
            label="Montant Total",
            placeholder="0.0",
            fieldstate=self.state.fieldstate("m_total")
        )
        m_total.text_entry.configure(width=250)
        m_total.grid(row=1, column=0, sticky="nsew", padx=5)

        # m_payer
        m_payer = TextInput(
            master=self.vesersement_container,
            label="Montant Payer",
            placeholder="0.0",
            fieldstate=self.state.fieldstate("m_payer")
        )
        m_payer.text_entry.configure(width=240)
        m_payer.grid(row=1, column=1, sticky="nsew", padx=5)

        # m_payer
        date_end = TextInput(
            master=self.vesersement_container,
            label="Date",
            placeholder="0.0",
            fieldstate=self.state.fieldstate("date")
        )
        date_end.text_entry.configure(width=100)
        date_end.grid(row=1, column=2, sticky="nsew", padx=5)


class AddsScreen(BaseFrame):
    def __init__(self, master, presenter, *args, **kwargs):
        super().__init__(master=master, *args, **kwargs)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        # form state
        self.state = DataFormState(master=self)
        self.presenter = presenter

        #
        scrollframe = ctk.CTkScrollableFrame(
            self, fg_color="transparent", bg_color="transparent")
        scrollframe.grid(row=0, column=0, sticky="nsew")

        # container
        self.container = BaseFrame(scrollframe, width=350)
        self.container.pack_propagate(False)
        self.container.pack()

        self.title = ctk.CTkLabel(
            master=self.container, text="Enregistrement du client", font=("", 20, "bold"))
        self.title.grid(row=0, column=0, sticky=tk.W, pady=(25, 10), padx=15)

        self.form = FormContainer(self.container, state=self.state)
        self.form.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        button = Button(
            self.container, text="Enregistrer", corner_radius=200, command=self.on_save)
        button.grid(row=2, column=0, sticky=tk.E, padx=15, pady=10)

    def on_save(self):
        if self.state.is_valide():
            data = self.state.values()
            data.pop("m_rest")
            _newdate = datetime.strptime(
                str(data.pop("date", "")), FORMAT_DATE)
            self.presenter.add_contrat(**data, date=_newdate.date())
            self.state.reset()
