
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window

Window.clearcolor = (0.05, 0.07, 0.12, 1)

class CyberSafetyApp(App):
    def build(self):
        layout = BoxLayout(
            orientation="vertical",
            padding=25,
            spacing=20
        )

        title = Label(
            text="[b]I AM DAD[/b]",
            markup=True,
            font_size=35
        )

        subtitle = Label(
            text="Cyber Safety System",
            font_size=20
        )

        button = Button(
            text="Cyber Safety Tips",
            font_size=22,
            size_hint=(1, 0.25)
        )

        layout.add_widget(title)
        layout.add_widget(subtitle)
        layout.add_widget(button)

        return layout

CyberSafetyApp().run()
