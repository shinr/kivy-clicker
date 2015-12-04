from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.properties import ObjectProperty
from kivy.vector import Vector
from ui.buttons import MenuButton, BaseButton
from ui.labels import BaseLabel
import strings

class BaseLayoutBehaviour(object):
	root = ObjectProperty(None)
	resources = ObjectProperty(None)
	root_parent = ObjectProperty(None)
	initializable = True
	scrollable = False
	def add_widget(self, widget, **kwargs):
		widget.root = self.root
		widget.resources = self.resources
		super(BoxLayout, self).add_widget(widget, **kwargs)

class MenuLayout(BoxLayout, BaseLayoutBehaviour):
	def __init__(self, **kwargs):
		super(MenuLayout, self).__init__(**kwargs)
		
	def initialize(self):
		self.add_widget(MenuButton(menu=strings.SCREEN_MAIN_GAMEPLAY, text=strings.descriptions[strings.SCREEN_MAIN_GAMEPLAY]))
		self.add_widget(MenuButton(menu=strings.SCREEN_UPGRADES, text=strings.descriptions[strings.SCREEN_UPGRADES]))
		self.add_widget(MenuButton(menu=strings.SCREEN_QUESTS, text=strings.descriptions[strings.SCREEN_QUESTS]))
		self.add_widget(MenuButton(menu=strings.SCREEN_OPTIONS, text=strings.descriptions[strings.SCREEN_OPTIONS]))
		self.add_widget(MenuButton(menu=strings.SCREEN_SHIP, text=strings.descriptions[strings.SCREEN_SHIP]))
		if self.root.debug_mode:
			self.add_widget(MenuButton(menu=strings.SCREEN_DEBUG, text=strings.descriptions[strings.SCREEN_DEBUG]))

	def add_widget(self, widget, **kwargs):
		widget.root = self.root
		widget.resources = self.resources
		super(BoxLayout, self).add_widget(widget, **kwargs)

class BasePopUpBehaviour(BaseLayoutBehaviour):
	def close(self, *args):
		self.root_parent.unlock(self)
		self.root_parent.remove_widget(self)

class ResetPopUp(StackLayout, BasePopUpBehaviour):
	def __init__(self, **kwargs):
		super(ResetPopUp, self).__init__(**kwargs)

	def initialize(self):
		self.add_widget(BaseLabel(text="Are you sure you want to reset?\nYou will lose all progress!", size_hint=(1, .6)))
		self.add_widget(BaseButton(text="OK", on_press=self.root.reset, size_hint=(.5, .2)))
		self.add_widget(BaseButton(text="Cancel", on_press=self.close, size_hint=(.5, .2)))

# dumb test class
class PopUpMenu(BoxLayout, BaseLayoutBehaviour):
	def __init__(self, **kwargs):
		super(PopUpMenu, self).__init__(**kwargs)

	def initialize(self):
		self.add_widget(BaseButton(on_press=self.close))

	


