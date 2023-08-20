from flet import *


class _Navigator:
    def page(self, page: Page):
        self._page = page

    def push(self, pageWidget):
        rount = f"/{len(self._page.views)}"
        self._page.views.append(View(route=rount, controls=[pageWidget]))
        self._page.go(rount)
        try:
            self._page.views[len(self._page.views) - 1].controls[0].init()
        except:
            pass
        print(len(self._page.views))

    def push_and_remove(self, pageWidget):
        for i in self._page.views:
            try:
                i.dispose()
            except:
                pass
        self._page.views.clear()
        self.push(pageWidget)

    def pop(self):
        try:
            self._page.views[len(self._page.views) - 1].controls[0].dispose()
        except:
            pass
        self._page.views.pop()
        self._page.update()


_navigator = _Navigator()


def page(page: Page):
    _navigator.page(page)


def push(pageWidget: Page):
    _navigator.push(pageWidget)


def push_and_remove(pageWidget: Page):
    _navigator.push_and_remove(pageWidget)


def pop():
    _navigator.pop()
