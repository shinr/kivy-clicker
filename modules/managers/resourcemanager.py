# resource 
from kivy.event import EventDispatcher
from kivy.properties import NumericProperty
from utils import strings

class ResourceManager(EventDispatcher):
	crew = NumericProperty(10.0)
	score = NumericProperty(0.0)
	dps = NumericProperty(0.0)
	click_power = NumericProperty(1.0)
	resources = {}
	def __init__(self, **kwargs):
		self.register_event_type('on_starclicker_resource_update')
		super(ResourceManager, self).__init__(**kwargs)
		self.resources = {
			strings.DEFAULT:-1,
			strings.RESOURCE_SCIENCE:self.score,
			strings.RESOURCE_CREW:self.crew, 
			strings.RESOURCE_DPS:self.dps,
			strings.RESOURCE_SHIP_COMMAND:0
		}
		self.dps = 1.0

	def bind_event(self, targets):
		for target in targets:
			self.bind(on_starclicker_resource_update=target)

	def update(self, dt):
		self.resources[strings.RESOURCE_SCIENCE] += self.dps * dt

	def on_starclicker_resource_update(self, resource, value):
		pass