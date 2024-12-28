import flet as ft
from login_view import LoginView
from connect_view import ConnectView

def main(page: ft.Page):
    # Theme
    theme = ft.Theme(font_family="Montserrat")
    # Page transition (when switching between views) on all devices
    theme.page_transitions.android = ft.PageTransitionTheme.NONE
    theme.page_transitions.ios = ft.PageTransitionTheme.NONE
    theme.page_transitions.macos = ft.PageTransitionTheme.NONE
    theme.page_transitions.linux = ft.PageTransitionTheme.NONE
    theme.page_transitions.windows = ft.PageTransitionTheme.NONE

    page.theme = theme
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 0

    def route_changed(e):
        route = e.route
        if route == "/login":
            page.views.append(LoginView())
        if route == "/connect":
            page.views.append(ConnectView())
        else:
            page.go("/login")
        # update views
        page.update()

    page.on_route_change = route_changed
    page.go("/login")


ft.app(main, assets_dir="assets")
