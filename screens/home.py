import win32api
from random import randint
from tkinter import filedialog, messagebox
from typing import Callable, List, Optional, Dict, Any, Tuple, Union, Protocol

from widgets.BaseFrame import BaseFrame
from widgets.containers.HomeContainer import HomeContainer
from widgets.containers.HomeInfo import HomeInfo
from db.services import ClientDataParser
from consts.datas import LIST_COLOMN

INTSTR = Union[str, int]
TITLE_BX = "Confirmation"
MSG_BX = "Voulez-vous vraiment supprimer?"
FIELD_DEFAULT_NAME = "name"


def get_initialfile(name: Optional[str] = None) -> str:
    idx = randint(298887, 778849392883948)
    name = (name or "unknow").replace(" ", "_")
    return f"{name }_{idx}"


class Presenter(Protocol):
    def get_contrats(self) -> List[List[INTSTR]]:
        ...

    def search_contrats(self, text: str) -> List[List[INTSTR]]:
        ...

    def delete_contrats(self, iids: List[INTSTR]) -> Union[int, None]:
        ...


class HomeState:
    """state state"""
    datas: List[List[INTSTR]] = []
    selecteds: List[INTSTR] = []
    privious: Union[INTSTR, None] = None

    def __init__(self, presenter: Presenter) -> None:
        self.presenter = presenter
        self.load_datas()

    def load_datas(self,) -> None:
        self.setdatas(self.presenter.get_contrats())

    def search_datas(self, text):
        self.setdatas(self.presenter.search_contrats(text=text))

    def remove_datas(self, idx: List[INTSTR]):
        iids = ClientDataParser.get_content_fields(data=self.datas, idx=idx)
        if self.presenter.delete_contrats(iids=iids):
            self.remove(iids)

    @property
    def is_selected(self) -> bool:
        return len(self.selecteds) > 0

    def setdatas(self, datas) -> None:
        self.datas = datas

    def set_selected(self, idx: Union[Tuple[INTSTR], List[INTSTR]]) -> None:
        self.privious = self.get_first_selected() or idx[0]
        self.selecteds = list(idx)

    def reset_selected(self) -> None:
        self.selecteds = []
        self.privious = None

    def get_first_selected(self) -> Union[str, int, None]:
        if self.is_selected:
            return self.selecteds[0]

    @property
    def is_same(self) -> bool:
        first = self.get_first_selected()
        return first is not None and (first == self.privious)

    @property
    def select_infos(self) -> dict:
        if selected := self.get_first_selected():
            return ClientDataParser.array_todict(
                data=self.datas[int(selected)],
                fields=dict(LIST_COLOMN)
            )
        return {}

    def remove(self, idx: Union[Tuple[INTSTR], List[INTSTR]]) -> None:
        _datas = [data for index, data in enumerate(
            self.datas) if index not in idx]
        self.datas = _datas


class HomeScreen(BaseFrame):
    infoscreenstate = False
    privious_selected: int | str | None = None
    datas: list[list[str]] = []
    selected_data: Optional[Dict[str, Any]] = {}

    def __init__(
        self,
        master,
        presenter,
        showinfo: Optional[Callable[[int | str], None]] = None,
        *args, **kwargs
    ):
        super().__init__(master, *args, **kwargs)

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.presenter = presenter
        self.state = HomeState(presenter=presenter)
        self.showinfo = showinfo

        # home container
        self.homecontainer = HomeContainer(
            master=self,
            onrefrech=self._refrech,
            onsearch=self._search,
            showinfo=self.showinfoscreen,
            ondelete=self._delete_contrats
        )
        self.homecontainer.grid(row=0, column=0, sticky="nsew")
        self.homecontainer.inserdata(self.state.datas)

        # home info wigdet
        self.infoscreen = HomeInfo(
            master=self,
            closeinfo=self.closeinfoscreen,
            onsave=self._onsave,
            onsaveprint=self._onsaveprint,
            fg_color=None,
            width=400
        )
        self.infoscreen.grid_propagate(False)

    def _delete_contrats(self, data: List[str | int]) -> int | None:
        if messagebox.askyesno(TITLE_BX, MSG_BX):
            self.state.remove_datas(data)
            self.homecontainer.refresh(self.state.datas)

    def _refrech(self):
        self.state.load_datas()
        self.homecontainer.refresh(self.state.datas)

    def _search(self, text):
        self.state.search_datas(text)
        self.homecontainer.refresh(self.state.datas)

    def save_process(self,) -> str | None:
        if not self.state.is_selected:
            return
        # name of client
        contrat = self.state.select_infos
        if pathname := filedialog.asksaveasfilename(
            initialfile=get_initialfile(name=contrat.get(FIELD_DEFAULT_NAME)),
            initialdir=self.presenter.config.docfolder,
            defaultextension=".pdf",
            filetypes=[
                ("Document pdf", "*.pdf"),
            ],
        ):
            return self.presenter.save_as_pdf(pathname=pathname, contrat=contrat)

    def _onsave(self) -> None:
        self.save_process()

    def _onsaveprint(self):
        if success := self.save_process():
            try:
                win32api.ShellExecute(
                    0, "print", success, None, ".", 0)  # type: ignore
            except Exception as e:
                print(e)

    def closeinfoscreen(self):
        """Close info screen"""
        self.infoscreenstate = False
        self.infoscreen.grid_forget()
        self.state.reset_selected()

    def select_data(self):
        selection = self.homecontainer.selection()
        self.state.set_selected(selection)

    def _refresh_infos(self) -> None:
        self.infoscreen.refrechitem(**self.state.select_infos)

    def showinfoscreen(self, iid: int | str) -> None:
        """Show screen info """
        self.select_data()
        if not self.infoscreenstate:
            return self._showinfostate()
        if self.state.is_same:
            self.closeinfoscreen()
            return
        self._refresh_infos()

    def _showinfostate(self):
        self.infoscreenstate = True
        self._refresh_infos()
        self.infoscreen.grid_propagate(False)
        self.infoscreen.grid(row=0, column=1, sticky="nswe")
        return
