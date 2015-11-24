from kivy.app import App
from kivy.clock import Clock
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from objects import ClickButton, ResourcesHandler
from ui import ScoreLabel

class GameLayout(Widget):
	def on_touch_down(self, touch):
		for child in self.children:
			if child.dispatch('on_touch_down', touch):
				return True

	def update(self, dt):
		for child in self.children:
			try:
				child.update(dt)
			except AttributeError:
				pass


class ClickerGameApp(App):
	def build(self):
		layout = GameLayout()
		mainScoreLabel = ScoreLabel(pos=(50, 350))
		layout.add_widget(mainScoreLabel)
		resourceHandler = ResourcesHandler(mainScoreLabel)
		layout.add_widget(ClickButton(resourceHandler, pos=(50, 50)))
		
		Clock.schedule_interval(layout.update, 1.0 / 60.0)
		return layout

if __name__ == '__main__':
	game = ClickerGameApp()
	game.run()