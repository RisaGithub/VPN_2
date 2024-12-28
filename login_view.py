import flet as ft


class MyTextField(ft.TextField):
    def __init__(self, multiline=True, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.border_color = ft.colors.TRANSPARENT
        self.focused_border_color = ft.colors.with_opacity(1, "#234ae2")
        self.text_size = 20
        self.border_radius = 20
        self.bgcolor = ft.colors.with_opacity(0.08, "white")
        self.content_padding = ft.padding.symmetric(horizontal=30, vertical=15)
        self.multiline = multiline
        self.hint_style = ft.TextStyle(color=ft.colors.with_opacity(0.5, "white"))


class LoginView(ft.View):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def build(self):
        self.bgcolor = ft.colors.with_opacity(1, "#030611")
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.padding = 0
        self.controls = [
            ft.Container(
                ft.Column(
                    [
                        ft.Text("Добро пожаловать!", size=25, opacity=1),
                        ft.Text("Вход", size=25),
                        ft.Column(
                            [
                                MyTextField(hint_text="Введите логин"),
                                MyTextField(hint_text="Введите пароль"),
                                ft.Container(height=15),
                                ft.ElevatedButton(
                                    text="Войти",
                                    style=ft.ButtonStyle(
                                        bgcolor=ft.colors.with_opacity(0.5, "#ba6bff"),
                                        color="white",
                                        shape=ft.RoundedRectangleBorder(radius=15),
                                        text_style=ft.TextStyle(size=25),
                                        padding=ft.padding.symmetric(15, 35),
                                    ),
                                    on_click=lambda _: self.page.go("/connect"),
                                ),
                                ft.Container(height=50),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            expand=True,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    expand=True,
                ),
                expand=True,
                gradient=ft.LinearGradient(
                    begin=ft.alignment.top_center,
                    end=ft.alignment.bottom_center,
                    colors=[
                        ft.colors.with_opacity(1, "#0f0f34"),
                        ft.colors.with_opacity(1, "#03030f"),
                    ],
                ),
                padding=60,
            )
        ]
