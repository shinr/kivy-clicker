from ui.buttons.basebutton import BaseButton
from utils.events import event_list

class ClickButton(BaseButton):
	initializable = False
	def on_starclicker_clickbutton_pressed(self, *args):
		pass

	def __init__(self, **kwargs):
		for e in event_list:
			self.register_event_type(e)
		super(ClickButton, self).__init__(**kwargs)
		

	def button_pressed(self, instance, **kwargs):
		self.dispatch("on_starclicker_clickbutton_pressed")
		self.root_parent.dispatch("on_starclicker_resource_update", 'res', 1)

	def on_starclicker_resource_update(self, resource, value):
		pass

