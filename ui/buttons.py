from kivy.uix.button import Button
from kivy.properties import ObjectProperty, NumericProperty, StringProperty

class BaseButton(Button):
	root = ObjectProperty(None)
	resources = ObjectProperty(None)

class PurchaseButton(BaseButton):
	pass

class MenuButton(BaseButton):
	menu = StringProperty("")
	def __init__(self, menu="", **kwargs):
		super(MenuButton, self).__init__(**kwargs)
		self.menu = menu
		self.bind(on_press=self.changeScreen)

	def changeScreen(self, instance):
		self.root.ChangeScreen(self.menu)