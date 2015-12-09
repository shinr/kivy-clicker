# misc components'
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, NumericProperty
from kivy.graphics import Rectangle

class BaseWidget(Widget):
	game_logic = ObjectProperty(None)
	root = ObjectProperty(None)
	root_parent = ObjectProperty(None)
	scrollable = False

class SliderItem(BaseWidget):
	pass


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