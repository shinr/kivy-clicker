# ui.py

from kivy.uix.label import Label
from kivy.properties import ObjectProperty, NumericProperty, StringProperty
import math
import strings

class BaseLabel(Label):
	root = ObjectProperty(None)
	game_logic = ObjectProperty(None)
	root_parent = ObjectProperty(None)
	initializable = False
	scrollable = False

class AttributeLabel(BaseLabel):
	text_mask = StringProperty('')
	attribute = StringProperty('')
	def __init__(self, attribute=strings.DEFAULT, text='Not properly updating {0}', **kwargs):
		super(AttributeLabel, self).__init__(**kwargs)
		self.attribute = attribute
		self.text_mask = text
		self.text = ''

	def update(self, dt):
		self.text = self.text_mask.format(self.game_logic.get_attribute_by_string(self.attribute))
		

