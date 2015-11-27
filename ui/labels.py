# ui.py

from kivy.uix.label import Label
from kivy.properties import ObjectProperty, NumericProperty, StringProperty
import math
import strings

class BaseLabel(Label):
	root = ObjectProperty(None)
	resources = ObjectProperty(None)

class CrewLabel(BaseLabel):
	crew = NumericProperty(0)
	def __init__(self, property='default', **kwargs):
		super(CrewLabel, self).__init__(**kwargs)
		self.text = "If you can see this, I'm not properly updating!"

	def update(self, dt):
		self.score = self.resources.get_attribute_by_string(strings.RESOURCE_CREW)
		self.text = "Science: " + str(math.floor(self.score))

class ScoreLabel(BaseLabel):
	score = NumericProperty(0.0)
	def __init__(self, **kwargs):
		super(ScoreLabel, self).__init__(**kwargs)
		self.text = "If you can see this, I'm not properly updating!"

	def update(self, dt):
		self.score = self.resources.get_attribute_by_string(strings.RESOURCE_SCIENCE)
		self.text = "Science: " + str(math.floor(self.score))


