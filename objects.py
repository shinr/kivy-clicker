from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty, NumericProperty
from kivy.graphics import Rectangle
from kivy.vector import Vector
from kivy.event import EventDispatcher
from ui.buttons import BaseButton
from ui.labels import BaseLabel
import strings 

class BaseWidget(Widget):
	resources = ObjectProperty(None)
	root = ObjectProperty(None)

class Upgrade(BaseWidget):
	price = NumericProperty(0)
	def __init__(self, **kwargs):
		super(BaseWidget, self).__init__(**kwargs)

	def initialize(self,description_text='This is template', button_position=(.1, .1), price=1):
		x, y = button_position[0],button_position[1]
		self.parent.add_widget(BaseLabel(text=description_text, pos_hint={'x':x, 'y':y}, size_hint=(.1, .1)))
		self.parent.add_widget(BaseButton(text=str(price), pos_hint={'x':x+.2, 'y':y}, size_hint=(.2, .1)))


class ResourcesHandler(EventDispatcher):
	crew = NumericProperty(0.0)
	score = NumericProperty(0.0)
	dps = NumericProperty(0.0)
	resources = {}
	def __init__(self, **kwargs):
		super(ResourcesHandler, self).__init__(**kwargs)
		self.resources = {
			strings.DEFAULT:-1,
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

				
class ClickButton(BaseWidget):
	def __init__(self, resourceHandler, **kwargs):
		super(ClickButton, self).__init__(**kwargs)
		self.resources = resourceHandler

	def on_touch_down(self, touch):
		if touch.x > self.pos[0] and touch.x < self.pos[0] + self.size[0]:
			if touch.y > self.pos[1] and touch.y < self.pos[1] + self.size[1]:
				self.resources.update_resource_by_value(strings.RESOURCE_SCIENCE, 1)