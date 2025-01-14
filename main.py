from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class Calculator(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)

        self.result = TextInput(
            text="0", halign="right", font_size=55, multiline=False, readonly=True
        )
        self.add_widget(self.result)

        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "C", "+"],
        ]

        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(text=label, font_size=32)
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            self.add_widget(h_layout)

        equals_button = Button(text="=", font_size=32)
        equals_button.bind(on_press=self.on_solution)
        self.add_widget(equals_button)

    def on_button_press(self, instance):
        current = self.result.text
        button_text = instance.text

        if button_text == "C":
            self.result.text = "0"
        else:
            if current == "0":
                self.result.text = button_text
            else:
                self.result.text += button_text

    def on_solution(self, instance):
        try:
            self.result.text = str(eval(self.result.text))
        except Exception:
            self.result.text = "Error"


class CalculatorApp(App):
    def build(self):
        return Calculator()


if __name__ == "__main__":
    CalculatorApp().run()