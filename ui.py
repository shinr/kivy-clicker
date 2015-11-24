# ui.py

from kivy.uix.label import Label
from kivy.properties import ObjectProperty, NumericProperty

class ScoreLabel(Label):
	resources = ObjectProperty(None)
	score = NumericProperty(0)
	def __init__(self, **kwargs):
		super(ScoreLabel, self).__init__(**kwargs)
		self.text = "Science: " + str(self.score)

	def updateScore(self, amount):
		self.score += amount
		self.text = "Science: " + str(self.score)