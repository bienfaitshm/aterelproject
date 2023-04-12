from typing import Any, List, Optional, Callable
from consts.datas import LIST_COLOMN
from widgets.BaseFrame import BaseFrame
from widgets.containers.HomeListContainer import HeaderList, HomeList, HomeListContainer


class HomeContainer(BaseFrame):
    def __init__(
        self,
        master: Any,
        onsearch: Optional[Callable[[str], None]] = None,
        onrefrech:  Optional[Callable[[], None]] = None,
        showinfo: Optional[Callable[[int | str], None]] = None,
        ondelete: Optional[Callable[[List[int | str]], int | None]] = None,
        *args, **kwargs
    ) -> None:
        super().__init__(master, *args, **kwargs)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # props
        self.onsearch = onsearch
        self.onrefresh = onrefrech
        self.showinfo = showinfo
        self.ondelete = ondelete

        self.homelist = HomeListContainer(
            master=self,
            header=self.create_header,
            listview=self.create_listview
        )

        self.homelist.grid(row=0, column=0, sticky="nswe")

    def selection(self):
        return self.listview.selection()

    def create_header(self, master) -> BaseFrame:
        self.header = HeaderList(
            master=master, height=90, search=self.onsearch, refresh=self.onrefresh)
        return self.header

    def create_listview(self, master) -> BaseFrame:
        self.listview = HomeList(master=master, column=dict(
            LIST_COLOMN), showinfo=self.showinfo, ondelete=self.delete_data)
        return self.listview

    def delete_data(self, data: List[int | str]):
        if self.ondelete and self.ondelete(data):
            self.listview.deleteitem(tuple(data))

    def getitem_selected(self):
        return self.listview.selection()

    def inserdata(self, datas: list[list[str | int]]) -> None:
        self.listview.inserdata(datas)

    def refresh(self, datas:  list[list[str | int]]) -> None:
        self.listview.removealldata()
        self.inserdata(datas)
