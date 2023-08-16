from flet import *
from flet import NavigationBar
import flet as ft
import navigator



class Home(UserControl):
    def __init__(self):
        super().__init__()
        self.textView = Text("Goto Login", size=25, color="black")
        self.txt_number = ft.TextField(
            value="0", text_align=ft.TextAlign.RIGHT, width=100
        )
        self.dlg = ft.AlertDialog(
            modal=True,
            title=ft.Text("Please confirm"),
            content=ft.Text("Do you really want to delete all those files?"),
            actions=[
                ft.TextButton("Yes", on_click=lambda _: self.close_dlg()),
                ft.TextButton("No", on_click=lambda _: self.close_dlg()),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
            on_dismiss=lambda e: print("Modal dialog dismissed!"),
        )

    def close_dlg(e):
        e.dlg.open = False
        e.page.update()

    def open_dlg(e):
        e.page.dialog = e.dlg
        e.dlg.open = True
        e.page.update()

    def minus_click(e):
        e.txt_number.value = str(int(e.txt_number.value) - 1)
        e.txt_number.update()

    def plus_click(e):
        e.txt_number.value = str(int(e.txt_number.value) + 1)
        e.txt_number.update()

    def toLogin(self):
        from login import Login

        navigator.pust(Login())

    def build(self):
        return ft.SafeArea(
            content=Column(
                controls=[
                    ft.Row(
                        [
                            ft.Container(
                                content=ft.IconButton(
                                    ft.icons.REMOVE,
                                    on_click=lambda _: self.minus_click(),
                                ),
                                on_long_press=lambda _: self.open_dlg(),
                            ),
                            self.txt_number,
                            ft.IconButton(
                                ft.icons.ADD, on_click=lambda _: self.plus_click()
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    Container(
                        bgcolor="red",
                        content=Column(
                            controls=[
                                Text("Welcome to the homepage"),
                                Container(
                                    on_click=lambda _: self.toLogin(),
                                    content=self.textView,
                                ),
                            ],
                        ),
                    ),
                ]
            )
        )
