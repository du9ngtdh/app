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

    def push_and_remove(self, pageWidget):
        for i in range(self._page.views):
            try:
                i.dispose()
            except:
                pass
        self._page.views.clear()
        rount = f"/{self.count}"
        self._page.views.append(View(route=rount, controls=[pageWidget]))
        self._page.go(rount)
        self.count += 1

    def pop(self):
        try:
            self._page.views[len(self._page.views) - 1].controls[0].dispose()
        except:
            pass

        self._page.views.remove(self._page.views[len(self._page.views) - 1])
        self._page.go(self._page.views[len(self._page.views) - 1].route)


_navigator = _Navigator()


def page(page: Page):
    _navigator.page(page)


def push(pageWidget: Page):
    _navigator.push(pageWidget)


def push_and_remove(pageWidget: Page):
    _navigator.push_and_remove(pageWidget)


def pop():
    _navigator.pop()
