from kivy.uix.screenmanager import ScreenManager
from kivy.properties import ObjectProperty
from kivy.clock import Clock
from modules.managers.resourcemanager import ResourceManager
from modules.controllers.gamecontroller import GameController
# class that manages the base views
class LayoutManager(ScreenManager):
    resources = ObjectProperty(None)
    game_logic = ObjectProperty(None)
    loadedScreens = []
    debug_mode = False
    def __init__(self, debug_mode=True, **kwargs):
        super(LayoutManager, self).__init__(**kwargs)
        self.resources = ResourceManager()
        self.game_logic = GameController(debug=debug_mode, resources=self.resources, layout_manager=self)
        Clock.schedule_interval(self.game_logic.update, 1.0 / 60.0)

    # overload for setting some new stuff
    def add_widget(self, screen, **kwargs):
        screen.layout.root = self
        screen.game_logic = self.game_logic
        screen.initialize()
        self.loadedScreens.append(screen)
        super(LayoutManager, self).add_widget(screen, **kwargs)

    def change_screen(self, target):
        self.current = target

    def update(self, dt):
        self.game_logic.update(dt)
        
    def reset(self, instance):
        print("I was reset!")