from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.stencilview import StencilView
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

class UpgradeList(RelativeLayout, StencilView):
	upgrades = []
	initializable = True
	upgrade_list_layout = ObjectProperty(None)
	def __init__(self, **kwargs):
		super(UpgradeList, self).__init__(**kwargs)
		for i in range(0, 4):
			self.upgrades.append(Upgrade()) 
		self.upgrade_list_layout= BoxLayout(orientation='vertical', size_hint=(.9, .14 * i), spacing=10)

	def initialize(self):
		i = 0
		for u in self.upgrades:
			i += 1
			self.upgrade_list_layout.add_widget(u)
			u.initialize(description_text='Upgrade no. {0}'.format(str(i)))
		self.add_widget(self.upgrade_list_layout)

	def update(self, dt):
		for c in self.children:
			c.pos = Vector(*(0, 1)) + c.pos # movement test

class Upgrade(BoxLayout, StencilView):
	price = NumericProperty(0)
	initializable = False
	def __init__(self, **kwargs):
		super(Upgrade, self).__init__(**kwargs)
		

	def initialize(self,description_text='This is template', price=1):
		self.add_widget(BaseLabel(text=description_text, size_hint=(.7, .90)))
		self.add_widget(BaseButton(text=str(price), size_hint=(.3, .90)))
		


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
	initializable = False
	def __init__(self, resourceHandler, **kwargs):
		super(ClickButton, self).__init__(**kwargs)
		self.resources = resourceHandler

	def on_touch_down(self, touch):
		if touch.x > self.pos[0] and touch.x < self.pos[0] + self.size[0]:
			if touch.y > self.pos[1] and touch.y < self.pos[1] + self.size[1]:
				self.resources.update_resource_by_value(strings.RESOURCE_SCIENCE, 1)