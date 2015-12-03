from kivy.app import App
from kivy.clock import Clock
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.vector import Vector
from objects import ResourcesHandler, Upgrade, UpgradeList, ProgressBarLayout
from ui.buttons import MenuButton, ClickButton
from ui.labels import ScoreLabel, BaseLabel, AttributeLabel
from ui.layouts import MenuLayout
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager, Screen
import strings

class LayoutHandler(ScreenManager):
	resources = ObjectProperty(None)
	loadedScreens = []
	debug_mode = False
	def __init__(self, debug_mode=True, **kwargs):
		super(LayoutHandler, self).__init__(**kwargs)
		self.resources = ResourcesHandler()
		Clock.schedule_interval(self.update, 1.0 / 60.0)
		self.debug_mode = debug_mode

	# overload for setting some new stuff
	def add_widget(self, screen, **kwargs):
		screen.resources = self.resources
		screen.layout.root = self
		screen.initialize()
		self.loadedScreens.append(screen)
		super(LayoutHandler, self).add_widget(screen, **kwargs)

	def ChangeScreen(self, target):
		self.current = target

	def update(self, dt):
		self.resources.update(dt)
		self.current_screen.layout.update(dt)

def convert_from_width_to_height(width, ratio=1.7777):
	return width / ratio

def convert_from_height_to_width(height, ratio=1.7777):
	return height * ratio
# to set up a layout for a screen, use the initialize method
# this could be 
class BaseScreen(Screen):
	layout = ObjectProperty(None)
	resources = ObjectProperty(None)
	def __init__(self, **kwargs):
		super(BaseScreen, self).__init__(**kwargs)
		self.layout = GameLayout(size=(600, 800))

	def initialize(self):
		self.layout.resources = self.resources
		self.add_widget(self.layout)
		self.layout.add_widget(MenuButton(menu=strings.SCREEN_MAIN_GAMEPLAY, text=strings.descriptions[strings.SCREEN_MAIN_GAMEPLAY], pos_hint={'x':0.0, 'y':.92}))
		self.layout.add_widget(BaseLabel(text="Layout not initialized!"))
		

class MainGameplayScreen(BaseScreen):
	def initialize(self):
		self.layout.resources = self.resources
		self.add_widget(self.layout)
		self.layout.add_widget(AttributeLabel(attribute=strings.RESOURCE_SCIENCE, text='Science {0}', pos_hint={'x':.5, 'y':.7}, size_hint=(.20, .05)))	
		self.layout.add_widget(ClickButton(self.resources, pos_hint={'x':.3, 'y':.1}, size_hint=(.4, convert_from_width_to_height(.4))))
		self.layout.add_widget(MenuLayout(pos_hint={'x':0, 'y':.92}))
		self.layout.add_widget(ProgressBarLayout(0.0, 10.0, tracked_attribute=strings.RESOURCE_SCIENCE, pos_hint={'x':.1, 'y':.52}, size_hint=(.7, .05)))
		

class OptionsScreen(BaseScreen):
	def initialize(self):
		self.layout.resources = self.resources
		self.add_widget(self.layout)
		self.layout.add_widget(BaseLabel(text="Here's some cool options"))
		self.layout.add_widget(MenuLayout(pos_hint={'x':0, 'y':.92}))
		

# loads a list of upgrades from xml and creates a browsable list
class UpgradeScreen(BaseScreen):
	def initialize(self):
		self.layout.resources = self.resources
		self.add_widget(self.layout)
		self.layout.add_widget(BaseLabel(text="Here's some cool upgrades"))
		self.layout.add_widget(UpgradeList(pos_hint={'x':.05, 'y':.0}, size_hint=(.9, .8)))
		self.layout.add_widget(MenuLayout(pos_hint={'x':0, 'y':.92}))
		

# lists quests and tracks their status, assign crew to quests to earn massive amounts of science
class QuestScreen(BaseScreen):
	pass

# bunch of variables to control
class DebugScreen(BaseScreen):
	pass

# ship contains a graph of subsystems you can assign crew to, these boost your science dps
class ShipScreen(BaseScreen):
	pass

class GameLayout(FloatLayout):
	root = ObjectProperty(None)
	old_pos = Vector(0, 0)
	def __init__(self, **kwargs):
		super(GameLayout, self).__init__(**kwargs)

	def on_touch_down(self, touch):
		new_pos = Vector(touch.x, touch.y)
		self.old_pos = new_pos
		for child in self.children:
			if child.dispatch('on_touch_down', touch):
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
		widget.resources = self.resources
		super(GameLayout, self).add_widget(widget, **kwargs)
		if widget.initializable:
			widget.initialize()
		


class ClickerGameApp(App):
	def build(self):
		handler = LayoutHandler()
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