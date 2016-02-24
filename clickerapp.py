from functools import partial
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.vector import Vector
from objects import ResourcesHandler, GameLogic
from ui.buttons import MenuButton, ClickButton, BaseButton
from ui.labels import BaseLabel, AttributeLabel
from ui.layouts import ProgressBarLayout, MenuLayout, PopUpMenu, UpgradeList
from ui import layouts
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager, Screen
import strings



		

def convert_from_width_to_height(width, ratio=1.7777):
	return width / ratio

def convert_from_height_to_width(height, ratio=1.7777):
	return height * ratio


		

		


class GameLayout(FloatLayout):
	root = ObjectProperty(None)
	old_pos = Vector(0, 0)
	locked = False
	lock_requested_by = ObjectProperty(None)
	def __init__(self, **kwargs):
		super(GameLayout, self).__init__(**kwargs)

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
		


class ClickerGameApp(App):
	def build(self):
		handler = LayoutManager()
		handler.add_widget(MainGameplayScreen(name=strings.SCREEN_MAIN_GAMEPLAY))
		handler.add_widget(OptionsScreen(name=strings.SCREEN_OPTIONS))
		handler.add_widget(QuestScreen(name=strings.SCREEN_QUESTS))
		handler.add_widget(UpgradeScreen(name=strings.SCREEN_UPGRADES))
		handler.add_widget(DebugScreen(name=strings.SCREEN_DEBUG))
		handler.add_widget(ShipScreen(name=strings.SCREEN_SHIP))
		return handler

if __name__ == '__main__':
	Config.set('graphics', 'resizable', '1')
	Config.set('graphics', 'width', '450')
	Config.set('graphics', 'height', '800')
	game = ClickerGameApp()
	game.run()