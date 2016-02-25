from kivy.properties import ObjectProperty
from kivy.uix.label import Label

class BaseLabel(Label):
	root = ObjectProperty(None)
	game_logic = ObjectProperty(None)
	root_parent = ObjectProperty(None)
	initializable = False
	scrollable = False