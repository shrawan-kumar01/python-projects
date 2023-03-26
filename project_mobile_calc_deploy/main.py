from ast import main
from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout  
from kivy.uix.button import Button as btn
from kivy.uix.textinput import TextInput

  
class MainApp(App):
    def built(self):
        self.icon = "calculator_icon.png"
        self.operators = ["+","-","*","*"]
        self.last_was_operator = None
        self.last_button = None

        main_layout = BoxLayout(oriantation = "vertical")
        self.sollution_scr = TextInput(background_color = "black", forground_color = "white")

        main_layout.add_widget(self.sollution_scr) # inside   OUR MAIN LAYOUT PASS SELF.SOLLUTUION_SCR

        button = [
            ["7","8","9","/"],
            ["4","5","6","*"],
            ["1","2","3","-"],
            [".","0","c","+"]

        ]

        for row in button:
            h_layout = BoxLayout()
            for label in row:
                button = button(
                    text = label,font_size = 30 , background_color = "grey",
                    pos_hint = {"center_x":0.5,"center_y" :0.5 },
                )
                button.bind(on_press = self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)

        equal_button = button(
            text = "=",font_size = 30 , background_color = "grey",
                    pos_hint = {"center_x":0.5,"center_y" :0.5 },


        )
        main_layout.add_widget(equal_button)
        return main_layout
        

if __name__ == "__main__":
    app = MainApp()
    app.run()