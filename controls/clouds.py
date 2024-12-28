import flet as ft
import random
import time


class CloudsControl(ft.Container):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def build(self):
        self.bgcolor = ft.colors.with_opacity(0, "#F2F2F2")
        
        self.content = ft.Container(
                content=ft.Image(
                    src="images/clouds/clouds_no_bg.gif",
                    fit=ft.ImageFit.COVER,
                    repeat=ft.ImageRepeat.NO_REPEAT,
                    opacity=0.8,
                ),
            )
