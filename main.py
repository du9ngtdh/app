
from flet import *
from home import Home
import navigator


def main(page: Page):
    page.theme_mode = "dark"
    navigator.page(page)
    navigator.push(Home())

app(target=main, host="192.168.1.4",port=8551, view = AppView.WEB_BROWSER)


