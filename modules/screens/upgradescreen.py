# loads a list of upgrades from xml and creates a browsable list
class UpgradeScreen(BaseScreen):
    def initialize(self):
        super(UpgradeScreen, self).initialize()
        self.layout.add_widget(UpgradeList(pos_hint={'x':.01, 'y':.01}, size_hint=(.9, .8)))
        self.layout.add_widget(MenuLayout(pos_hint={'x':0, 'y':.92}))
