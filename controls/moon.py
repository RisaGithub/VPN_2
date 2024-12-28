import flet as ft


class MoonControl(ft.Container):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def build(self):
        size = 180
        self.content = ft.Container(
            content=ft.Image(
                src="images/moon.gif",
                fit=ft.ImageFit.COVER,
                repeat=ft.ImageRepeat.NO_REPEAT,
                border_radius=ft.border_radius.all(500),
                opacity=0.3,
                
            ),
            width=size,
            height=size,
            border_radius=ft.border_radius.all(500),
            shadow=ft.BoxShadow(
                blur_radius=20,
                color=ft.colors.BLUE_GREY_300,
                offset=ft.Offset(0, 0),
                blur_style=ft.ShadowBlurStyle.OUTER,
            ),
            bgcolor="#ba6bff",
            border=ft.BorderSide(width=5, color="white"),
        )
