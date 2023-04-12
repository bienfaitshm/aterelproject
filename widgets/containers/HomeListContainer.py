import tkinter as tk
import customtkinter as ctk
from tkinter import ttk
from typing import List, Optional, Callable, Any
from widgets.BaseFrame import BaseFrame
from widgets.Image import Image
from widgets.SearchInput import SearchInput

DB_CLICK_EVT = '<Double-Button-1>'
RETURN_EVT = "<Return>"
DELETE_EVT = "<Delete>"


class HeaderList(BaseFrame):
    def __init__(
            self,
            master,
            search: Optional[Callable[[str], None]] = None,
            refresh: Optional[Callable[[], None]] = None,
            *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.grid_propagate(False)
        self.columnconfigure(0, weight=1)

        self.refresh = refresh

        # container
        self.container = BaseFrame(self)
        self.container.grid(row=0, column=0, sticky="nsew")

        self.actioncontainer = BaseFrame(self)
        self.actioncontainer.grid(row=1, column=0, sticky="es")

        # search
        self.search = SearchInput(
            self.container, onsubmit=search, corner_radius=100, height=50, width=350)
        self.search.pack_propagate(False)
        self.search.pack()

        self.refreshbtn = ctk.CTkButton(
            self.actioncontainer,
            text="",
            width=25,
            height=25,
            border_width=0,
            corner_radius=5,
            fg_color="transparent",
            command=self._refresh,
            image=Image(
                light_image="icons8-update-left-rotation-100.png", size=(17, 17))
        )
        self.refreshbtn.grid_propagate(False)
        self.refreshbtn.grid(row=1, column=0, sticky="es", padx=10, pady=10)

    def _refresh(self):
        if self.refresh:
            self.refresh()


class HomeList(BaseFrame):
    def __init__(
        self,
        master=any,
        showinfo: Optional[Callable[[int | str], None]] = None,
        ondelete: Optional[Callable[[List[str | int]], int | None]] = None,
        column: Optional[dict[str, Any]] = None,
        *args, **kwargs
    ) -> None:
        super().__init__(master, *args, **kwargs)

        # config
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # props
        self.column = column or {}
        self.showinfo = showinfo
        self.ondelete = ondelete

        # main container
        self.container = BaseFrame(self)
        self.container.rowconfigure(0, weight=1)
        self.container.columnconfigure(0, weight=1)
        self.container.grid(row=0, column=0, sticky="nsew")

        # tree view
        self.treeview = ttk.Treeview(
            self.container, columns=list(self.column.keys()), style="mystyle.Treeview")
        self.treeview.grid(row=0, column=0, sticky="nsew", padx=5)

        # adding a scroll y
        self._add_yscrollbar()
        self._configstyle()
        self._create_column()  # create column keys of tree
        self._create_header()  # create header of tree
        self._bind_event()  # bind event
        self.tagconfig()  # tag config color

    def inserdata(self, data: list):
        for iid, values in enumerate(data):
            self.treeview.insert(
                parent='',
                index='end',
                iid=str(iid),
                text="",
                values=values,
                tags=self.get_tags_colors(iid)
            )

    def removealldata(self):
        self.treeview.delete(*self.treeview.get_children())

    def deleteitem(self, *args):
        self.treeview.delete(*args)

    def _delete_item_evt(self, event) -> None:
        print("On dddd", )
        if self.ondelete:
            self.ondelete(list(self.selection()))

    def selection(self):
        return self.treeview.selection()

    def _showinfo(self, event=None):
        selected = self.treeview.selection()
        if self.showinfo is not None:
            self.showinfo(selected[0])

    def _add_yscrollbar(self,):
        """ adding a y scroll bar to tree view """
        tree_scrolly = ctk.CTkScrollbar(
            self.container, orientation=tk.VERTICAL, command=self.treeview.yview)
        tree_scrolly.grid(row=0, column=1, sticky="ns")
        self.treeview.config(yscrollcommand=tree_scrolly.set)

    def _create_header(self) -> None:
        """Create header tree view """
        self.treeview.heading("#0", text="", anchor=tk.CENTER)
        for key, headname in self.column.items():
            self.treeview.heading(key, text=str(headname), anchor=tk.CENTER)

    def _create_column(self) -> None:
        """Create column tree view"""
        self.treeview.column("#0", width=0, stretch=tk.NO)
        for col in self.column.keys():
            self.treeview.column(
                col, anchor=tk.CENTER, minwidth=50, width=100)

    def _bind_event(self) -> None:
        # self.treeview.bind('<<TreeviewSelect>>', self.on_select)
        self.treeview.bind(DB_CLICK_EVT, self._showinfo)
        self.treeview.bind(RETURN_EVT, self._showinfo)
        self.treeview.bind(DELETE_EVT, self._delete_item_evt)

    def _configstyle(self) -> None:
        """Config a style to tree View"""
        style = ttk.Style()
        style.configure(
            "mystyle.Treeview",
            background="#3E3E3E",
            foreground="black",
            rowheight=40,
            fieldbackground="silver",
            highlightthickness=0,
            bd=10,
            font=('Calibri', 11)
        )  # Modify the font of the body
        style.map("mystyle.Treeview", background=[
            ("selected", "#237C56")
        ])

        style.configure(
            "mystyle.Treeview.Heading", font=('Calibri', 10, ''), background="#3E3E3E")  # Modify the font of the headings
        style.layout(
            "mystyle.Treeview", [
                ('mystyle.Treeview.treearea', {
                    'sticky': 'nswe'
                })
            ])  # Remove the borders

    def get_tags_colors(self, idx: int):
        return ('odd',) if idx % 2 == 0 else ('even',)

    def tagconfig(self):
        """tags config"""
        self.treeview.tag_configure(
            'odd', background='#75B58E', foreground="white")
        self.treeview.tag_configure('even', background='#BADAC7')


class HomeListContainer(BaseFrame):
    def __init__(
        self,
        master,
        header: Callable[[Any], BaseFrame],
        listview: Callable[[Any], BaseFrame],
        *args, **kwargs
    ) -> None:
        super().__init__(master, *args, **kwargs)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        # header
        self.header = header(self)
        self.header.grid(row=0, column=0, sticky="nswe", pady=(30, 0))

        # list view
        self.listview = listview(self)
        self.listview.grid(row=1, column=0, sticky="nswe")
