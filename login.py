from flet import *


import navigator


class Login(UserControl):
    def __init__(self):
        super().__init__()

    
    def dispose(self):
        print("Disposing")
    
    def init(self):
        print("init")

    def toHome(self):
        from home import Home

        # navigator.pust(Home())
        navigator.pop()

    def build(self):
        return Column(
            controls=[
                Container(
                    bgcolor="blue",
                    content=Column(
                        controls=[
                            Text("Welcome back \n This is the login pages"),
                            Container(
                                on_click=lambda _: self.toHome(),
                                content=Text("Goto Home", size=25, color="black"),
                            ),
                        ]
                    ),
                )
            ]
        )
