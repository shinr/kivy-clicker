from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.stencilview import StencilView
from kivy.properties import ObjectProperty, NumericProperty, StringProperty
from kivy.graphics import Rectangle
from kivy.vector import Vector
from kivy.event import EventDispatcher
from ui.buttons import BaseButton
from ui.labels import BaseLabel
import strings 
import math

class BaseWidget(Widget):
	resources = ObjectProperty(None)
	root = ObjectProperty(None)
	root_parent = ObjectProperty(None)
	scrollable = False

class SliderItem(BaseWidget):
	pass

class UpgradeList(RelativeLayout, StencilView):
	upgrades = []
	initializable = True
	upgrade_list_layout = ObjectProperty(None)
	scrollable = True
	current_scroll = NumericProperty(0.0)
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
			c.pos = Vector(*(0, self.current_scroll)) + c.pos
		if not self.current_scroll == 0.0:
			self.current_scroll *= .95
			if abs(self.current_scroll) < .1:
				self.current_scroll = 0.0

	def scroll(self, scroll):
		self.current_scroll = scroll

class Upgrade(BoxLayout, StencilView):
	price = NumericProperty(0)
	initializable = False
	def __init__(self, **kwargs):
		super(Upgrade, self).__init__(**kwargs)
		

	def initialize(self,description_text='This is template', price=1):
		self.add_widget(BaseLabel(text=description_text, size_hint=(.7, .90)))
		self.add_widget(BaseButton(text=str(price), size_hint=(.3, .90)))
		

class Bar(BaseWidget):
	progress = NumericProperty(0.0)
	_rect = ObjectProperty(None)
	_length = NumericProperty(0)
	def __init__(self, bar_length=100, **kwargs):
		super(BaseWidget, self).__init__(**kwargs)
		self._length=bar_length
		self.bind(progress=self.update_canvas)
		self.bind(_length=self.update_canvas)
		with self.canvas:
			self._rect = Rectangle(pos=self.pos, size=(10, 10))

	def update_canvas(self, *args):
		self._rect.pos = self.pos
		self._rect.size = (0 + self._length * self.progress, 10)


class ProgressBarLayout(BoxLayout):
	start = NumericProperty(0.0)
	current = NumericProperty(0.0)
	end = NumericProperty(0.0)
	tracked_attribute = StringProperty(None)
	_bar = ObjectProperty(None)
	initializable = False
	scrollable = False
	def __init__(self, start=0.0, end=1.0, bar_length=0, tracked_attribute=strings.DEFAULT, **kwargs):
		super(ProgressBarLayout, self).__init__(orientation='vertical', **kwargs)
		self.start, self.end = start, end
		self.tracked_attribute = tracked_attribute
		if bar_length==0:
			self.bind(width=self.update_bar)
		self._bar = Bar(pos=self.pos, bar_length=bar_length)
		self.add_widget(BaseLabel(text=str(self.tracked_attribute)))
		self.add_widget(self._bar)

	def update_bar(self, *args):
		self._bar._length=self.width * self.size_hint[0]

	def update(self, dt):
		attr = self.resources.get_attribute_by_string(self.tracked_attribute)
		if attr != self.current:
			self.current = attr
			self._bar.progress = max(min((self.current - self.start) / (self.end - self.start), 1.0), 0.0)

		


class ResourcesHandler(EventDispatcher):
	crew = NumericProperty(10.0)
	score = NumericProperty(0.0)
	dps = NumericProperty(0.0)
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

	def get_attribute_by_string(self, attribute):
		if attribute in self.resources:
			return self.resources[attribute]
		return -1

	def update_resource_by_value(self, resource_key, resource_value, *args): 
		self.resources[resource_key] += resource_value

	def move_resource_by_amount(self, move_from, move_to, amount, *args):
		if self.resources[move_from] >= amount:
			self.resources[move_from] -= amount
			self.resources[move_to] += amount
		else:
			pass # maybe notify someone

	def update(self, dt):
		self.resources[strings.RESOURCE_SCIENCE] += self.dps * dt

				
