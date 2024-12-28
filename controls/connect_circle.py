import flet as ft
import time

CONNECT_CIRCLE_SIZE = 270


class ConnectCircle(ft.Container):
    def __init__(self, animate_func, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.animate_func = animate_func

    def build(self):
        self.connect_status_control = ft.Text("Подключиться", visible=False, size=CONNECT_CIRCLE_SIZE/10)
        self.circle_container = ft.Container(
            ft.Column(
                [self.connect_status_control],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            border_radius=200,
            border=ft.border.all(2, ft.colors.WHITE),
            width=CONNECT_CIRCLE_SIZE,
            height=CONNECT_CIRCLE_SIZE,
            on_click=self.start_connect,
            shadow=ft.BoxShadow(
                blur_radius=13,
                color=ft.colors.BLUE_GREY_300,
                offset=ft.Offset(0, 0),
                blur_style=ft.ShadowBlurStyle.OUTER,
            ),
        )
        self.connect_circle_stack = ft.Stack([self.circle_container])

        self.content = ft.Container(
            ft.Column(
                [
                    ft.Column([ft.Container(height=1)]),
                    ft.Text("mamavpluse".upper(), color="#ba6bff", size=22, weight=ft.FontWeight.W_700),
                    ft.Container(height=10),
                    self.connect_circle_stack,
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

    def start_connect(self, e=None):
        if self.connect_status_control.value != "Подключено":
            # change circle to connection...
            pr = ft.ProgressRing(
                width=CONNECT_CIRCLE_SIZE,
                height=CONNECT_CIRCLE_SIZE,
                stroke_width=4,
                color="white",
            )

            self.circle_container.border = None
            self.connect_circle_stack.controls.append(pr)
            self.connect_status_control.value = "Подключение..."
            self.page.update()

            time.sleep(2)
            # connection finished

            # change circle to connected
            pr.visible = False
            connected_color = "#ba6bff"
            self.circle_container.shadow.color = connected_color
            self.connect_status_control.color = connected_color
            self.circle_container.shadow.blur_radius = 20
            self.connect_status_control.value = "Подключено"
            self.circle_container.border = ft.border.all(3, connected_color)
            pr.color = "white"

            # animate everything
            self.animate_func()

        else:
            self.circle_container.shadow.color = "white"
            self.connect_status_control.color = "white"
            self.circle_container.shadow.blur_radius = 13
            self.connect_status_control.value = "Подключиться"
            self.circle_container.border = ft.border.all(
                3, ft.colors.with_opacity(1, "white")
            )
            self.animate_func(hide=True)

        # update page
        self.page.update()
