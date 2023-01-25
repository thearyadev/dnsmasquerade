import flet as ft
from typing import Callable


class ListItem(ft.UserControl):
    def __init__(self, name, addr, on_long_press: Callable, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name, self.addr = name, addr
        self.on_long_press = on_long_press

    def build(self):
        return ft.ListTile(
            leading=ft.Icon(ft.icons.NETWORK_PING),
            title=ft.Row(
                [
                    ft.Text(self.name),
                    ft.Container(
                        content=ft.Icon(name=ft.icons.REMOVE),
                        padding=ft.Padding(left=0, top=25, right=0, bottom=0)
                    )
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            ),
            subtitle=ft.Row(
                [
                    ft.Icon(
                        name=ft.icons.ARROW_FORWARD,
                    ),
                    ft.Text(
                        self.addr
                    ),
                ]
            ),
            on_long_press=self.on_long_press
        )
