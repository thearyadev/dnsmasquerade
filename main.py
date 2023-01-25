import flet as ft
from gui import (
    AppHeading,
    ListItem,
)
import dnsmasq


def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.add(
        ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        AppHeading("dnsmasquerade"),
                        ft.ListView(
                            expand=1,
                            spacing=10,
                            padding=20,
                            auto_scroll=False,
                            controls=[
                                ListItem(
                                    **entry,
                                    on_long_press=lambda _: print("deleting")
                                ) for entry in dnsmasq.getEntries()
                            ]
                        )
                    ]
                ),
                width=400,
                padding=15,
            ),
            width=600,
            height=600
        )
    )

    page.update()


if __name__ == '__main__':
    ft.app(target=main, view=ft.WEB_BROWSER)
