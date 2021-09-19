from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


def calculate_state(state):
    if state:
        convert = 'km'
    else:
        convert = 'miles'
    return convert


class Unit_convert(App):
    """ SquareNumberApp is a Kivy App for squaring a number """
    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (300, 200)
        self.title = "Km to miles Converter"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def km_calculate(self,value,state):
        if state == 1:
            result = value * 1.609
        else:
            result = value / 1.609
        self.root.ids.output_label.text = str("{:.2f}".format(result))

Unit_convert().run()
