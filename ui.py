# ui.py

from kivy.uix.label import Label
from kivy.properties import ObjectProperty, NumericProperty
import math

class ScoreLabel(Label):
	resources = ObjectProperty(None)
	score = NumericProperty(0.0)
	def __init__(self, resourceHandler, **kwargs):
		super(ScoreLabel, self).__init__(**kwargs)
		self.resources = resourceHandler
		self.text = "Science: " + str(self.score)

	def update(self, dt):
		self.score = self.resources.getCurrentScore()
		self.text = "Science: " + str(math.floor(self.score))

	def updateScore(self, amount):
		self.score = amount
		self.text = "Science: " + str(math.floor(self.score))