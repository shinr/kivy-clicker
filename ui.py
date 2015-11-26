# ui.py

from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.properties import ObjectProperty, NumericProperty, StringProperty
import math

class BaseLabel(Label):
	root = ObjectProperty(None)
	resources = ObjectProperty(None)

class BaseButton(Button):
	root = ObjectProperty(None)
	resources = ObjectProperty(None)

class ScoreLabel(BaseLabel):
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

class MenuButton(BaseButton):
	menu = StringProperty("")
	def __init__(self, menu="", **kwargs):
		super(MenuButton, self).__init__(**kwargs)
		self.menu = menu
		self.bind(on_press=self.changeScreen)

	def changeScreen(self, instance):
		self.root.ChangeScreen(self.menu)

"""
	def on_touch_down(self, touch):
		if touch.x > self.pos[0] and touch.x < self.pos[0] + self.size[0]:
			if touch.y > self.pos[1] and touch.y < self.pos[1] + self.size[1]:
				pass
"""