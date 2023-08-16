
from flet import *
from home import Home
import navigator
import numpy


def main(page: Page):
    page.theme_mode = "dark"
    navigator.page(page)
    navigator.pust(Home())

app(target=main, view= AppView.WEB_BROWSER)



