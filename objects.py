from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, NumericProperty
from kivy.graphics import Rectangle
from kivy.vector import Vector
from kivy.event import EventDispatcher

class ResourcesHandler(EventDispatcher):
	crew = NumericProperty(0.0)
	score = NumericProperty(0.0)
	dps = NumericProperty(0.0)
	def __init__(self, **kwargs):
		super(ResourcesHandler, self).__init__(**kwargs)
		self.dps = 1.0

	def updateScoreByClickValue(self):
		self.score += 1

	def getCurrentScore(self):
		return self.score

	def update(self, dt):
		self.score += self.dps * dt


class MenuButton(Widget):
	my_layout = ObjectProperty(None)
	def __init__(self, **kwargs):
		super(MenuButton, self).__init__(**kwargs)

	def on_touch_down(self, touch):
		self.pos = Vector(10, 0) + self.pos

class ClickButton(Widget):
	resources = ObjectProperty(None)
	def __init__(self, resourceHandler, **kwargs):
		super(ClickButton, self).__init__(**kwargs)
		self.resources = resourceHandler
		with self.canvas:
			Rectangle(size=(50, 50))
			self.bind(pos=self.update_canvas)
			self.bind(size=self.update_canvas)
		self.update_canvas()

	def update_canvas(self):
		self.canvas.clear()
		with self.canvas:
			Rectangle(pos=self.pos, size=self.size)

	def on_touch_down(self, touch):
		if touch.x > self.pos[0] and touch.x < self.pos[0] + self.size[0]:
			if touch.y > self.pos[1] and touch.y < self.pos[1] + self.size[1]:
				self.resources.updateScoreByClickValue()