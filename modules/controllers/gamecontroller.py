from kivy.event import EventDispatcher
from kivy.properties import ObjectProperty

# all game logic happens through this class	
class GameController(EventDispatcher):
	layout_manager = ObjectProperty(None)
	resources = ObjectProperty(None)
	debug_mode = False
	def __init__(self, debug=False, resources=None, layout_manager=None, **kwargs):
		super(GameController, self).__init__(**kwargs)
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