from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, NumericProperty
from kivy.graphics import Rectangle
from kivy.vector import Vector
from kivy.event import EventDispatcher
import strings 

class Upgrade():
	pass

class ResourcesHandler(EventDispatcher):
	crew = NumericProperty(0.0)
	score = NumericProperty(0.0)
	dps = NumericProperty(0.0)
	resources = {}
	def __init__(self, **kwargs):
		super(ResourcesHandler, self).__init__(**kwargs)
		self.resources = {
			strings.RESOURCE_SCIENCE:self.score,
			strings.RESOURCE_CREW:self.crew
		}
		self.dps = 1.0

	def get_attribute_by_string(self, attribute):
		if attribute in self.resources:
			return self.resources[attribute]
		return -1

	def update_resource_by_value(self, resource_key, resource_value):
		self.resources[resource_key] += resource_value

	def update(self, dt):
		self.resources[strings.RESOURCE_SCIENCE] += self.dps * dt


class BaseWidget(Widget):
	resources = ObjectProperty(None)
	root = ObjectProperty(None)
				
class ClickButton(BaseWidget):
	def __init__(self, resourceHandler, **kwargs):
		super(ClickButton, self).__init__(**kwargs)
		self.resources = resourceHandler

	def on_touch_down(self, touch):
		if touch.x > self.pos[0] and touch.x < self.pos[0] + self.size[0]:
			if touch.y > self.pos[1] and touch.y < self.pos[1] + self.size[1]:
				self.resources.update_resource_by_value(strings.RESOURCE_SCIENCE, 1)