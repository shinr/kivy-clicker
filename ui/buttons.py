from kivy.uix.button import Button
from kivy.properties import ObjectProperty, NumericProperty, StringProperty
import strings

class BaseButton(Button):
	root = ObjectProperty(None)
	resources = ObjectProperty(None)
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
		self.root.ChangeScreen(self.menu)

class ClickButton(BaseButton):
	initializable = False
	def __init__(self, resourceHandler, **kwargs):
		super(ClickButton, self).__init__(**kwargs)
		self.resources = resourceHandler

	def on_touch_down(self, touch):
		if touch.x > self.pos[0] and touch.x < self.pos[0] + self.size[0]:
			if touch.y > self.pos[1] and touch.y < self.pos[1] + self.size[1]:
				self.resources.update_resource_by_value(strings.RESOURCE_SCIENCE, 1)
		super(ClickButton, self).on_touch_down(touch)
		return True