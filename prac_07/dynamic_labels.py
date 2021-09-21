from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

NAMES = ["SANJAY NIELSEN-BETTS", "HARRY THE NON-WIZARD", "A STEREOTYPICAL VILLAIN"]


class DynamicLabels(App):
    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create widget from names in NAME and add them to the GUI."""
        for name in NAMES:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)


DynamicLabels().run()
