from typing import Optional
from frontend.jinja_templates import templates

class ItemBrowserObjectButton:
    def __init__(self):
        self.name: str = ""
        self.on_click_url: str = ""

class ItemBrowserObject:
    def __init__(self):
        self.title: str = "No title provided"
        self.on_click_url: Optional[str] = None

class ItemBrowser:
    def __init__(self,
                 name: str = "Unnamed item browser",
                 refresh_url: Optional[str] = None,
                 toolbar_buttons: Optional[list[ItemBrowserObjectButton]] = [],
                 objects: Optional[list[ItemBrowserObject]] = [],
                 ):
        self.name: str = name

        self.refresh_url: str = refresh_url
        self.toolbar_buttons: list[ItemBrowserObjectButton] = toolbar_buttons

        self.objects: list[ItemBrowserObject] = objects

    def render(self):
        return templates.TeplateResponse("apps/elements/object_browser.j2", {"browser" : self})
