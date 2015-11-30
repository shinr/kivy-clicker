from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.vector import Vector
from ui.buttons import MenuButton
import strings

class MenuLayout(BoxLayout):
	root = ObjectProperty(None)
	resources = ObjectProperty(None)
	initializable = True
	scrollable = False
	def __init__(self, **kwargs):
		super(MenuLayout, self).__init__(**kwargs)
		
	def initialize(self):
		self.add_widget(MenuButton(menu=strings.SCREEN_MAIN_GAMEPLAY, text=strings.descriptions[strings.SCREEN_MAIN_GAMEPLAY]))
		self.add_widget(MenuButton(menu=strings.SCREEN_UPGRADES, text=strings.descriptions[strings.SCREEN_UPGRADES]))
		self.add_widget(MenuButton(menu=strings.SCREEN_QUESTS, text=strings.descriptions[strings.SCREEN_QUESTS]))
		self.add_widget(MenuButton(menu=strings.SCREEN_OPTIONS, text=strings.descriptions[strings.SCREEN_OPTIONS]))

	def add_widget(self, widget, **kwargs):
		widget.root = self.root
		widget.resources = self.resources
		super(BoxLayout, self).add_widget(widget, **kwargs)

	
		

