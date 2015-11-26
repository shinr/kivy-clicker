from kivy.app import App
from kivy.clock import Clock
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from objects import ClickButton, ResourcesHandler
from ui import ScoreLabel, MenuButton, BaseLabel
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager, Screen
import strings

class LayoutHandler(ScreenManager):
	resources = ObjectProperty(None)
	loadedScreens = []
	def __init__(self, **kwargs):
		super(LayoutHandler, self).__init__(**kwargs)
		self.resources = ResourcesHandler()
		Clock.schedule_interval(self.update, 1.0 / 60.0)

	# overload for setting some new stuff
	def add_widget(self, screen, index=0, canvas=None):
		screen.resources = self.resources
		screen.layout.root = self
		screen.initialize()
		self.loadedScreens.append(screen)
		super(LayoutHandler, self).add_widget(screen)

	def ChangeScreen(self, target):
		self.current = target

	def update(self, dt):
		self.resources.update(dt)
		self.current_screen.layout.update(dt)

# using initialize method initialize the layout
class BaseScreen(Screen):
	layout = ObjectProperty(None)
	resources = ObjectProperty(None)
	def __init__(self, **kwargs):
		super(BaseScreen, self).__init__(**kwargs)
		self.layout = GameLayout(size=(600, 800))

	def initialize(self):
		self.layout.add_widget(MenuButton(menu=strings.SCREEN_MAIN_GAMEPLAY, text=strings.descriptions[strings.SCREEN_MAIN_GAMEPLAY], pos_hint={'x':0.0, 'y':.92}))
		self.layout.add_widget(BaseLabel(text="Layout not initialized!"))
		self.add_widget(self.layout)

class MainGameplayScreen(BaseScreen):
	def initialize(self):
		mainScoreLabel = ScoreLabel(self.resources, pos_hint={'x':.1, 'y':.15}, size_hint=(.20, .05))
		self.layout.add_widget(mainScoreLabel)	
		self.layout.add_widget(ClickButton(self.resources, pos_hint={'x':.36, 'y':.5}, size_hint=(.24, .24)))
		self.layout.add_widget(MenuButton(menu=strings.SCREEN_OPTIONS, text=strings.descriptions[strings.SCREEN_OPTIONS], pos_hint={'x':0.0, 'y':.92}))
		self.layout.add_widget(MenuButton(menu=strings.SCREEN_UPGRADES, text=strings.descriptions[strings.SCREEN_UPGRADES], pos_hint={'x':0.3, 'y':.92}))
		self.layout.add_widget(MenuButton(menu=strings.SCREEN_QUESTS, text=strings.descriptions[strings.SCREEN_QUESTS], pos_hint={'x':0.6, 'y':.92}))
		self.add_widget(self.layout)

class OptionsScreen(BaseScreen):
	def initialize(self):
		self.layout.add_widget(MenuButton(menu=strings.SCREEN_MAIN_GAMEPLAY, text=strings.descriptions[strings.SCREEN_MAIN_GAMEPLAY], pos_hint={'x':0.0, 'y':.92}))
		self.layout.add_widget(MenuButton(menu=strings.SCREEN_UPGRADES, text=strings.descriptions[strings.SCREEN_UPGRADES], pos_hint={'x':0.3, 'y':.92}))
		self.layout.add_widget(MenuButton(menu=strings.SCREEN_QUESTS, text=strings.descriptions[strings.SCREEN_QUESTS], pos_hint={'x':0.6, 'y':.92}))
		self.add_widget(self.layout)

class UpgradeScreen(BaseScreen):
	pass

class QuestScreen(BaseScreen):
	pass


class GameLayout(FloatLayout):
	root = ObjectProperty(None)
	def __init__(self, **kwargs):
		super(GameLayout, self).__init__(**kwargs)

	def on_touch_down(self, touch):
		for child in self.children:
			if child.dispatch('on_touch_down', touch):
				return True

	# update all widgets
	def update(self, dt):
		for child in self.children:
			try:
				child.update(dt)
			except AttributeError:
				pass

	# overload for injecting my own stuff
	def add_widget(self, widget, index=0, canvas=None):
		widget.root = self.root
		super(GameLayout, self).add_widget(widget, index=index)


class ClickerGameApp(App):
	def build(self):
		handler = LayoutHandler()
		handler.add_widget(MainGameplayScreen(name=strings.SCREEN_MAIN_GAMEPLAY))
		handler.add_widget(OptionsScreen(name=strings.SCREEN_OPTIONS))
		handler.add_widget(QuestScreen(name=strings.SCREEN_QUESTS))
		handler.add_widget(UpgradeScreen(name=strings.SCREEN_UPGRADES))
		return handler

if __name__ == '__main__':
	Config.set('graphics', 'resizable', '1')
	Config.set('graphics', 'width', '600')
	Config.set('graphics', 'height', '800')
	game = ClickerGameApp()
	game.run()