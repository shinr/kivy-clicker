from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.graphics import Rectangle
from kivy.vector import Vector

class MenuButton(Widget):
	my_layout = ObjectProperty(None)
	def __init__(self, **kwargs):
		super(MenuButton, self).__init__(**kwargs)

	def on_touch_down(self, touch):
		self.pos = Vector(10, 0) + self.pos

class ClickButton(Widget):
	def __init__(self, **kwargs):
		super(ClickButton, self).__init__(**kwargs)
		with self.canvas:
			Rectangle(size=(50, 50))

	def on_touch_down(self, touch):
		print ("touch me", self.pos)
		self.pos = Vector(10, 0) + self.pos