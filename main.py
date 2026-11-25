from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class IAmDadApp(App):
    def build(self):
        layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=15
        )

        layout.add_widget(Label(
            text="I AM DAD\nCyber Safety System",
            font_size=28
        ))

        options = [
            "Blackmail Help",
            "Save Evidence",
            "Report Cybercrime",
            "Safety Guide",
            "Emergency Help"
        ]

        for option in options:
            button = Button(
                text=option,
                font_size=18
            )
            button.bind(on_press=self.show_message)
            layout.add_widget(button)

        return layout

    def show_message(self, instance):
        messages = {
            "Blackmail Help": "Kisi bharosemand bade ko bataiye. Paise mat dijiye.",
            "Save Evidence": "Dhamki wale messages ko surakshit rakhiye.",
            "Report Cybercrime": "cybercrime.gov.in par report karein.",
            "Safety Guide": "Strong password aur 2-step verification use karein.",
            "Emergency Help": "Turant khatre mein 112 par call karein."
        }

        self.root.clear_widgets()
        self.root.add_widget(Label(
            text=messages[instance.text],
            font_size=20
        ))

if __name__ == "__main__":
    IAmDadApp().run()
