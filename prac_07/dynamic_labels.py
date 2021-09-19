from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

NAME = ["SANJAY NIELSEN-BETTS", "HARRY THE NON-WIZARD", "A STEREOTYPICAL VILLAIN"]


class DynamicLabels(App):
    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.py')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create widget from names in NAME and add them to the GUI."""
        for names in NAME:
            temp_label = Label(text=names)
            self.root.ids.main(temp_label)


DynamicLabels().run()
