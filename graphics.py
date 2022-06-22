import kivy
from kivy.app import App


class AbfrageApp(App):
    def __init__(self, cv: str):
        super().__init__()

        self.cv = cv

    def on_start(self):
        ...

    def on_click(self, btn_id):
        ...

    def on_print(self):
        ...