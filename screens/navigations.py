import tkinter as tk
from typing import Optional, Callable, Dict, List, Union, Any, Protocol

from screens.home import HomeScreen
from screens.setting import SettingScreen
from screens.adds import AddsScreen

from widgets.BaseFrame import BaseFrame
from widgets.Button import Button
from widgets.Image import Image


class Component(Protocol):
    def __call__(self, master: Union[tk.Misc, tk.Frame, Any], presenter: Any, *args, **kwargs) -> tk.Frame:
        ...


class Screen:
    def __init__(
        self,
        name: str,
        component: Component,
        default_screen: bool = False,
        component_props: Optional[Dict[str, Any]] = None
    ) -> None:
        if component_props is None:
            component_props = {}
        self.props = component_props
        self.name = name
        self.component = component
        self.default_screen = default_screen


class Navigator(BaseFrame):
    _screens: Dict[str, tk.Frame] = {}

    def __init__(self, master, screens: List[Screen], curent: str, presenter: Any, *args, **kwargs):
        super().__init__(master=master, *args, **kwargs)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.curent_screen: str = curent
        for screen in screens:
            self._screens[screen.name] = screen.component(
                master=self, presenter=presenter)

            if self.curent_screen is None:
                self.curent_screen = screen.name
            if screen.default_screen:
                self.curent_screen = screen.name

        self._change_frame(name=self.curent_screen)

    def navigate(self, name: str) -> None:
        if self.curent_screen == name:
            return
        self._change_frame(name=name)

    def _change_frame(self, name: str) -> None:
        self.unmount()
        if scr := self._screens.get(name):
            self.curent_screen = name
            scr.grid(row=0, column=0, sticky="nsew")

    def unmount(self):
        if self.curent_screen is None:
            return
        if scr := self._screens.get(self.curent_screen):
            scr.grid_forget()


class SideNavigation(BaseFrame):
    currentname: Optional[str] = None

    def __init__(self, master, currentscreen: str, navigate: Callable[[str], None], *args, **kwargs):
        super().__init__(master=master, *args, **kwargs)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.navigate = navigate
        self.currentname = currentscreen

        self.top = BaseFrame(self)
        self.bottom = BaseFrame(self)

        self.listbtn = Button(self.top,
                              text=None,
                              width=50,
                              command=lambda: self._navigate("list"),
                              fg_color="transparent",
                              image=Image(light_image="icons8-bullet-list-100.png",),)
        self.add = Button(self.top,
                          text=None,
                          width=50,
                          fg_color="transparent",
                          command=lambda: self._navigate("add"),
                          image=Image(light_image="icons8-new-copy-100.png",),)

        self.listbtn.grid(row=0, column=0, pady=5)
        self.add.grid(row=1, column=0, pady=5)

        self.settingbtn = Button(self.bottom,
                                 text=None,
                                 width=50,
                                 fg_color="transparent",
                                 command=lambda: self._navigate("setting"),
                                 image=Image(
                                     light_image="icons8-gear-100.png",),
                                 )
        self.settingbtn.grid(row=0, column=0)

        self.top.columnconfigure(0, weight=1)
        self.top.grid(row=0, column=0, sticky="nwe", pady=(50, 0))
        self.bottom.grid(row=1, column=0, sticky="swe", pady=(0, 20))
        self.bottom.columnconfigure(0, weight=1)

        self.screen = {
            "list": self.listbtn,
            "add": self.add,
            "setting": self.settingbtn
        }

        self.set_currentname("list")

    def config_color(self, color: str) -> None:
        if c := self.screen.get(self.currentname or ""):
            c.configure(fg_color=color)

    def set_currentname(self, name: str) -> None:
        if self.currentname:
            self.config_color("transparent")
        self.currentname = name
        self.config_color("#52AD80")

    def _navigate(self, name: str) -> None:
        if self.currentname == name:
            return
        self.set_currentname(name)
        self.navigate(name)


class Navigation(BaseFrame):
    current: str = "list"

    def __init__(self, master, presenter, *args, **kwargs):
        super().__init__(master=master, *args, **kwargs)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.presenter = presenter

        self.create_mainframe()
        self.create_sibebar()

    def create_mainframe(self):
        # Main Frame
        self.navigator = Navigator(self, screens=[
            Screen(name="list", component=HomeScreen),
            Screen(name="setting", component=SettingScreen),
            Screen(name="add", component=AddsScreen),
        ], curent=self.current, presenter=self.presenter)
        self.navigator.grid(row=0, column=1, sticky="nsew")

    def create_sibebar(self) -> None:
        # Side Frame
        self.side = SideNavigation(
            self, navigate=self.navigate, currentscreen=self.current, width=60, fg_color=None)
        self.side.grid(row=0, column=0, sticky="nsew", ipady=10, ipadx=5)

    def navigate(self, name: str) -> None:
        self.navigator.navigate(name)
