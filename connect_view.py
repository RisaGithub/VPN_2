import flet as ft
import time
from controls.moon import MoonControl
from controls.connect_circle import ConnectCircle
from controls.clouds import CloudsControl


class ConnectView(ft.View):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def build(self):
        part = 5
        self.HIDDEN_CLOUDS_TOP = self.page.height
        self.HIDDEN_CLOUDS_BOTTOM = - self.page.height // part
        self.SHOWN_CLOUDS_TOP = self.page.height - self.page.height // part
        self.SHOWN_CLOUDS_BOTTOM = -self.page.height // 40
        
        self.bgcolor = ft.colors.with_opacity(1, "#030611")
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.padding = 0

        self.moon_control = MoonControl(
            opacity=0.7, top=-250, left=-30, animate_position=1000
        )
        self.clouds_control = CloudsControl(
            bottom=-self.HIDDEN_CLOUDS_BOTTOM, right=0, top=self.HIDDEN_CLOUDS_TOP, left=0, animate_position=1000
        )
        self.connect_circle = ConnectCircle(animate_func=self.animate)
        self.back_btn = ft.IconButton(
            ft.icons.ARROW_BACK,
            icon_color="white",
            icon_size=30,
            padding=30,
            on_click=lambda _: self.page.go("/login"),
        )

        self.controls = [
            ft.Stack(
                [
                    self.connect_circle,
                    self.clouds_control,
                    self.moon_control,
                    self.back_btn,
                ],
                expand=True,
            )
        ]

    def did_mount(self):
        time.sleep(0.4)
        self.connect_circle.start_connect()
        return super().did_mount()

    def animate(self, hide=False):
        if hide:
            self.moon_control.top = -250
            self.clouds_control.top = self.HIDDEN_CLOUDS_TOP
        else:
            self.moon_control.top = 80
            self.clouds_control.bottom = self.SHOWN_CLOUDS_BOTTOM
            self.clouds_control.top = self.SHOWN_CLOUDS_TOP
