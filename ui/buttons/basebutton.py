from kivy.uix.button import Button
from kivy.properties import ObjectProperty

class BaseButton(Button):
	root = ObjectProperty(None)
	game_logic = ObjectProperty(None)
	root_parent = ObjectProperty(None)
	initializable = False
	scrollable = False

	def __init__(self, **kwargs):
		super(BaseButton, self).__init__(on_press=self.button_pressed, **kwargs)

	def button_pressed(self, instance, **kwargs):
		pass