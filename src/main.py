import flet as ft
import os
from core.db import init_db


def main(page: ft.Page):
    if os.getenv("PRIMEAPES_DEV"):
        page.window.width = 390
        page.window.height = 844

    counter = ft.Text("0", size=50, data=0)

    def increment_click(e: ft.Event[ft.FloatingActionButton]):
        counter.data += 1
        counter.value = str(counter.data)

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.ADD, key="increment", on_click=increment_click
    )
    page.add(
        ft.SafeArea(
            expand=True,
            content=ft.Container(
                content=counter,
                alignment=ft.Alignment.CENTER,
            ),
        )
    )


if __name__ == "__main__":
    init_db()
    ft.run(main)