from kivy.properties import StringProperty
from ui.labels.baselabel import BaseLabel
import utils.utils as utilities
from utils import strings
from utils.events import event_list, DefaultEventHandlers

class AttributeLabel(BaseLabel, DefaultEventHandlers):
	text_mask = StringProperty('')
	attribute = StringProperty('')
	def __init__(self, attribute=strings.DEFAULT, text='Not properly updating {0}', **kwargs):
		for e in event_list:
			self.register_event_type(e)
		super(AttributeLabel, self).__init__(**kwargs)
		self.attribute = attribute
		self.text_mask = text
		self.text = self.text_mask.format(0)

	def on_starclicker_resource_update(self, resource, value):
		#if self.attribute == resource:
		print ("eh")
		self.text = self.text_mask.format(value)
