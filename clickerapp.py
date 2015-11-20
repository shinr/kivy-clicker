from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import ObjectProperty
from objects import ClickButton

class GameLayout(RelativeLayout):
	def on_touch_down(self, touch):
		print ("toucvh", touch)
		for child in self.children:
			if child.dispatch('on_touch_down', touch):
				return True

class ClickerGameApp(App):
	
	def build(self):
		layout = GameLayout()
		layout.add_widget(ClickButton())
		return layout

if __name__ == '__main__':
	game = ClickerGameApp()
	game.run()