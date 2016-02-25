from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.vector import Vector

# base layout that handles input events and updates all it's views
class GameLayout(FloatLayout):
	root = ObjectProperty(None)
	old_pos = Vector(0, 0)
	locked = False
	lock_requested_by = ObjectProperty(None)
	def __init__(self, **kwargs):
		self.register_event_type('on_starclicker_resource_update')
		super(GameLayout, self).__init__(**kwargs)
		print (self.parent)

	# locking will not send actions except to the entity who requested the lock, until unlock
	def lock(self, requested):
		self.locked = True
		self.lock_requested_by = requested

	def unlock(self, requested):
		if requested == self.lock_requested_by:
			self.locked = False

	def on_touch_down(self, touch):
		new_pos = Vector(touch.x, touch.y)
		self.old_pos = new_pos
		for child in self.children:
			if self.locked:
				if child is self.lock_requested_by:
					if child.dispatch('on_touch_down', touch):
						return True
			elif child.dispatch('on_touch_down', touch):
				return True

	def on_touch_move(self, touch):
		new_pos = Vector(touch.x, touch.y)
		if not new_pos.x == self.old_pos.x or new_pos.y == self.old_pos.y:
			distance_y = new_pos.y - self.old_pos.y
			if distance_y > 1 or distance_y < -1:
				for c in [kid for kid in self.children if kid.scrollable == True]:
					c.scroll(distance_y)
		self.old_pos = new_pos

	# update all widgets
	def update(self, dt):
		for child in self.children:
			try:
				child.update(dt)
			except AttributeError:
				pass

	# overload for injecting my own stuff
	def add_widget(self, widget, **kwargs):
		widget.root = self.root
		widget.game_logic = self.game_logic
		widget.root_parent = self
		super(GameLayout, self).add_widget(widget, **kwargs)
		if widget.initializable:
			widget.initialize()

	def on_starclicker_resource_update(self, resource, value):
		for child in self.children:
			print(child)
			child.dispatch("on_starclicker_resource_update", 'res', 1)