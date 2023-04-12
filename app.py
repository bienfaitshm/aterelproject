import tkinter
import customtkinter as ctk
from services import pdfreport
from dataclasses import dataclass
from services.utility import resource_path
import settings
from typing import Dict, Optional, Union, Tuple, Protocol, List, Callable, Any
from screens.navigations import Navigation
from widgets.BaseFrame import BaseFrame
from db.services import ClientDataParser, ClientDBService
from consts import datas
from app_config import AppConfiguration


class IUi(Protocol):
    pass


class IModelService(Protocol):
    get_contrats: Callable[[], List[List[str]]]

# ctk.set_default_color_theme("medias/themes/blue.json")


class ModelService(IModelService):
    def __init__(self) -> None:
        self.db = ClientDBService()

    def get_contrats(self) -> List[List[str]]:
        return ClientDataParser.parser_for_treeview(clients=self.db.getclients(), fields=datas.LIST_COLOMN)

    def search_contrats(self, text: str) -> List[List[str]]:
        return ClientDataParser.parser_for_treeview(clients=self.db.searchclients(text=text), fields=datas.LIST_COLOMN)

    def add_contrat(self, *args, **kwargs):
        return self.db.createclient(client=kwargs)

    def delete_contrats(self, data: List[str | int]) -> int:
        return self.db.deleteclients(data)


class Presenter:
    def __init__(self, ui: IUi, model: ModelService) -> None:
        self.ui = ui
        self.model = model
        self.config = AppConfiguration()
        self.config.load_config()

    def get_contrats(self) -> List[List[str]]:
        return self.model.get_contrats()

    def search_contrats(self, text) -> List[List[str]]:
        return self.model.search_contrats(text=text)

    def delete_contrats(self, iids: List[str | int]) -> int:
        return self.model.delete_contrats(iids)

    def add_contrat(self, *args, **kwargs) -> Optional[Any]:
        self.model.add_contrat(*args, **kwargs)
        return

    def save_as_pdf(self, pathname: str, contrat: Dict[str, Any]) -> str:
        infos_reporter = pdfreport.ReportClientInfos(
            contrat_id=contrat.get("id", "Unknown"),
            adress=contrat.get("adress", "Unknown"),
            date=contrat.get("date", "Unknown"),
            email=contrat.get("email", "Unknown"),
            m_payer=contrat.get("m_payer", "Unknown"),
            m_rest=contrat.get("m_rest", "Unknown"),
            m_total=contrat.get("m_total", "Unknown"),
            name=contrat.get("name", "Unknown"),
            num_id=contrat.get("num_id", "Unknown"),
            num_impot=contrat.get("num_inpot", "Unknown"),
            num_p_id=contrat.get("num_p_id", "Unknown"),
            num_rccm=contrat.get("num_rccm", "Unknown"),
            tel=contrat.get("phone", "Unknown"),
        )
        pdf = pdfreport.PdfReport()
        pdf.create_document(infos=infos_reporter)
        pdfservice = pdfreport.PdfService(pdfreport=pdf)
        pdfservice.save(pathname)
        return pathname


class App(ctk.CTk):
    def __init__(self, fg_color: Optional[Union[str, Tuple[str, str]]] = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        # Window configuration
        self.wconfig()
        # Theme initialization
        self.theme_init()

    def wconfig(self) -> None:
        """ Window configuration """
        self.geometry(settings.SIZE_APP)
        self.iconbitmap(resource_path("icon.ico"))
        self.minsize(600, 500)
        self.title(settings.APP_NAME)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

    def theme_init(self) -> None:
        ctk.set_default_color_theme(settings.COLOR_THEME)

    def create_ui(self, presenter: Presenter) -> None:
        ctk.set_appearance_mode(presenter.config.theme)
        self.navigation = Navigation(master=self, presenter=presenter)
        self.navigation.grid(row=0, column=0, sticky="nsew")
        self.bottombar = BaseFrame(self, bg_color="green", height=25)
        self.bottombar.grid_propagate(False)
        self.bottombar.grid(row=1, column=0, sticky="ew")


def main():
    app = App()
    model = ModelService()
    presenter = Presenter(ui=app, model=model)
    app.create_ui(presenter)
    app.mainloop()


if __name__ == "__main__":
    main()
