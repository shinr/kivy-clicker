from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from ui.layouts.gamelayout import GameLayout
# to set up a layout for a screen, use the initialize method
# this could be 
class BaseScreen(Screen):
    layout = ObjectProperty(None)
    game_logic = ObjectProperty(None)
    def __init__(self, **kwargs):
        super(BaseScreen, self).__init__(**kwargs)
        self.layout = GameLayout(size=(600, 800))

    def initialize(self):
        self.layout.game_logic = self.game_logic
        self.add_widget(self.layout)
        
