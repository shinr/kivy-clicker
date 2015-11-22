from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from objects import ClickButton

class GameLayout(Widget):
	def on_touch_down(self, touch):
		for child in self.children:
			if child.dispatch('on_touch_down', touch):
				return True

class ClickerGameApp(App):
	
	def build(self):
		layout = GameLayout()
		layout.add_widget(ClickButton(pos=(50, 50)))
		return layout

if __name__ == '__main__':
	game = ClickerGameApp()
	game.run()