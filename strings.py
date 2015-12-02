from kivy.properties import StringProperty

SCREEN_MAIN_GAMEPLAY = "mainGameplayScreen"
SCREEN_UPGRADES = "upgradesScreen"
SCREEN_QUESTS = "questsScreen"
SCREEN_OPTIONS = "optionsScreen"
SCREEN_DEBUG = "debugScreen"
SCREEN_SHIP = "shipScreen"

descriptions = {
	SCREEN_OPTIONS:"Options",
	SCREEN_QUESTS:"Quests",
	SCREEN_MAIN_GAMEPLAY:"Main",
	SCREEN_UPGRADES:"Upgrades",
	SCREEN_DEBUG:"Debug",
	SCREEN_SHIP:"Ship"
}

debugOnly = {
	SCREEN_OPTIONS:False,
	SCREEN_QUESTS:False,
	SCREEN_MAIN_GAMEPLAY:False,
	SCREEN_UPGRADES:False,
	SCREEN_DEBUG:True,
	SCREEN_SHIP:False	
}

DEFAULT = 'default_string'
RESOURCE_SCIENCE = "res_science"
RESOURCE_CREW = "res_crew"
RESOURCE_DPS = "res_dps"