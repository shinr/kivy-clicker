# ui.py

from kivy.uix.label import Label
from kivy.properties import ObjectProperty, NumericProperty, StringProperty
import math
import strings

class BaseLabel(Label):
	root = ObjectProperty(None)
	resources = ObjectProperty(None)

class AttributeLabel(BaseLabel):
	text_mask = StringProperty('')
	attribute = StringProperty('')
	def __init__(self, attribute=strings.DEFAULT, text='Not properly updating {0}', **kwargs):
		super(AttributeLabel, self).__init__(**kwargs)
		self.attribute = attribute
		self.text_mask = text
		self.text = ''

	def update(self, dt):
		self.text = self.text_mask.format(self.resources.get_attribute_by_string(self.attribute))

class CrewLabel(BaseLabel):
	def __init__(self, property='default', **kwargs):
		super(CrewLabel, self).__init__(**kwargs)
		self.text = "If you can see this, I'm not properly updating!"

	def update(self, dt):
		self.score = self.resources.get_attribute_by_string(strings.RESOURCE_CREW)
		self.text = "Science: " + str(math.floor(self.resources.get_attribute_by_string(strings.RESOURCE_CREW)))

class ScoreLabel(BaseLabel):
	def __init__(self, **kwargs):
		super(ScoreLabel, self).__init__(**kwargs)
		self.text = "If you can see this, I'm not properly updating!"

	def update(self, dt):
		self.text = "Science: " + str(math.floor(self.resources.get_attribute_by_string(strings.RESOURCE_SCIENCE)))


