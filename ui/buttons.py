from kivy.uix.button import Button
from kivy.properties import ObjectProperty, NumericProperty, StringProperty
import strings

class BaseButton(Button):
	root = ObjectProperty(None)
	game_logic = ObjectProperty(None)
	root_parent = ObjectProperty(None)
	initializable = False
	scrollable = False

class PurchaseButton(BaseButton):
	pass

class MenuButton(BaseButton):
	menu = StringProperty("")
	def __init__(self, menu="", **kwargs):
		super(MenuButton, self).__init__(**kwargs)
		self.menu = menu
		self.bind(on_press=self.changeScreen)

	def changeScreen(self, instance):
		self.root.change_screen(self.menu)

class ClickButton(BaseButton):
	initializable = False
	def __init__(self, **kwargs):
		super(ClickButton, self).__init__(**kwargs)
		