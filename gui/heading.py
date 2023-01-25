import flet as ft


class AppHeading(ft.UserControl):
    def __init__(self, text, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.text = text

    def build(self):
        return ft.Row(
            controls=[
                ft.Text(
                    self.text,
                    size=30,
                    weight=ft.FontWeight.W_900,
                    selectable=True
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
