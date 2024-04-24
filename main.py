import flet as ft


def main(page: ft.Page):
    page.title="sastagram"
    page.bgcolor="black"
    page.navigation_bar=ft.CupertinoNavigationBar(destinations=[ft.NavigationDestination(icon=ft.icons.HOME, label="Home"),
                                                                ft.NavigationDestination(icon=ft.icons.ADD, label="Post"),
                                                                ft.NavigationDestination(icon=ft.icons.PERSON, label="Profile")],
                                                                bgcolor=ft.colors.TRANSPARENT,
                                                                border=ft.border.Border(top=ft.BorderSide(1, ft.colors.GREY_900), bottom=ft.BorderSide(0, ft.colors.GREY_900), left=ft.BorderSide(0, ft.colors.GREY_900), right=ft.BorderSide(0, ft.colors.GREY_900)),
                                                                inactive_color="grey",
                                                                active_color="white"
                                                                )


    page.add()

ft.app(main)