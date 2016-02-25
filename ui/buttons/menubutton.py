class MenuButton(BaseButton):
	menu = StringProperty("")
	def __init__(self, menu="", **kwargs):
		super(MenuButton, self).__init__(**kwargs)
		self.menu = menu
		self.bind(on_press=self.changeScreen)

	def changeScreen(self, instance):
		self.root.change_screen(self.menu)