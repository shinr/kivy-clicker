from kivy.app import App
from kivy.config import Config
from utils import strings
from modules.managers.layoutmanager import LayoutManager
from modules.screens.maingameplayscreen import MainGameplayScreen
#from modules.screens.debugscreen import DebugScreen
#from modules.

# main app, loads stuff
class ClickerGameApp(App):
	def build(self):
		handler = LayoutManager()
		handler.add_widget(MainGameplayScreen(name=strings.SCREEN_MAIN_GAMEPLAY))
		#handler.add_widget(OptionsScreen(name=strings.SCREEN_OPTIONS))
		#handler.add_widget(QuestScreen(name=strings.SCREEN_QUESTS))
		#handler.add_widget(UpgradeScreen(name=strings.SCREEN_UPGRADES))
		#handler.add_widget(DebugScreen(name=strings.SCREEN_DEBUG))
		#handler.add_widget(ShipScreen(name=strings.SCREEN_SHIP))
		return handler

if __name__ == '__main__':
	Config.set('graphics', 'resizable', '1')
	Config.set('graphics', 'width', '450')
	Config.set('graphics', 'height', '800')
	game = ClickerGameApp()
	game.run()