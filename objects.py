from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.stencilview import StencilView
from kivy.properties import ObjectProperty, NumericProperty, StringProperty
from kivy.vector import Vector
from kivy.event import EventDispatcher
from ui.buttons import BaseButton
from ui.labels import BaseLabel
import strings 
import math
import ui.layouts as layouts
from exceptions import *


# all game logic happens through this class	
class GameLogic(EventDispatcher):
	layout_manager = ObjectProperty(None)
	resources = ObjectProperty(None)
	debug_mode = False
	def __init__(self, debug=False, resources=None, layout_manager=None, **kwargs):
		super(GameLogic, self).__init__(**kwargs)
		self.debug_mode = debug
		if resources is None:
			raise ResourcesNotDefined("Resources is not defined (None)")
		self.resources = resources
		if resources is None:
			raise LayoutManagerNotDefined("LayoutManager is not defined (None)")
		self.layout_manager = layout_manager
		
	def update(self, dt):
		self.resources.update(dt)
		self.layout_manager.current_screen.layout.update(dt)

	def display_popup(self, instance, popup_name="", **kwargs):
		if hasattr(layouts, popup_name):
			popup = getattr(layouts, popup_name)(**kwargs)
			self.layout_manager.current_screen.layout.add_widget(popup)
			self.layout_manager.current_screen.layout.lock(popup)

	def change_screen(self, target):
		self.layout_manager.change_screen(target)

	def get_attribute_by_string(self, attribute):
		if attribute in self.resources.resources:
			return self.resources.resources[attribute]
		return -1

	def update_resource_by_value(self, resource_key, resource_value, *args): 
		self.resources.resources[resource_key] += resource_value

	def move_resource_by_amount(self, move_from, move_to, amount, *args):
		if self.resources.resources[move_from] >= amount:
			self.resources.resources[move_from] -= amount
			self.resources.resources[move_to] += amount
		else:
			raise ResourcesBelowZero()

	def add_click_science(self, instance):
		self.update_resource_by_value(strings.RESOURCE_SCIENCE, self.resources.click_power)

	def reset(self, instance):
		print ("i was reset")

class ResourcesHandler(EventDispatcher):
	crew = NumericProperty(10.0)
	score = NumericProperty(0.0)
	dps = NumericProperty(0.0)
	click_power = NumericProperty(1.0)
	resources = {}
	def __init__(self, **kwargs):
		super(ResourcesHandler, self).__init__(**kwargs)
		self.resources = {
			strings.DEFAULT:-1,
			strings.RESOURCE_SCIENCE:self.score,
			strings.RESOURCE_CREW:self.crew, 
			strings.RESOURCE_DPS:self.dps,
			strings.RESOURCE_SHIP_COMMAND:0
		}
		self.dps = 1.0

	def update(self, dt):
		self.resources[strings.RESOURCE_SCIENCE] += self.dps * dt

				
