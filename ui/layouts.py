from kivy.uix.boxlayout import BoxLayout

from kivy.uix.stacklayout import StackLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.stencilview import StencilView
from kivy.properties import ObjectProperty, NumericProperty, StringProperty
from kivy.vector import Vector
from ui.buttons import MenuButton, BaseButton
from ui.labels import BaseLabel, AttributeLabel
from ui.components import Bar
import strings




class BaseLayoutBehaviour(object):
	root = ObjectProperty(None)
	game_logic = ObjectProperty(None)
	root_parent = ObjectProperty(None)
	initializable = True
	scrollable = False
	def add_widget(self, widget, **kwargs):
		widget.root = self.root
		widget.game_logic = self.game_logic
		super(BaseLayoutBehaviour, self).add_widget(widget, **kwargs)

class UpgradeList(RelativeLayout, StencilView):
	upgrades = []
	initializable = True
	upgrade_list_layout = ObjectProperty(None)
	scrollable = True
	current_scroll = NumericProperty(0.0)
	def __init__(self, **kwargs):
		super(UpgradeList, self).__init__(**kwargs)
		for i in range(0, 4):
			self.upgrades.append(Upgrade()) 
		self.upgrade_list_layout= BoxLayout(orientation='vertical', size_hint=(.9, .14 * i), spacing=10)

	def initialize(self):
		i = 0
		for u in self.upgrades:
			i += 1
			self.upgrade_list_layout.add_widget(u)
			u.initialize(description_text='Upgrade no. {0}'.format(str(i)))
		self.add_widget(self.upgrade_list_layout)

	def update(self, dt):
		for c in self.children:
			c.pos = Vector(*(0, self.current_scroll)) + c.pos
		if not self.current_scroll == 0.0:
			self.current_scroll *= .95
			if abs(self.current_scroll) < .1:
				self.current_scroll = 0.0

	def scroll(self, scroll):
		self.current_scroll = scroll

class Upgrade(BoxLayout, StencilView):
	price = NumericProperty(0)
	initializable = False
	def __init__(self, **kwargs):
		super(Upgrade, self).__init__(**kwargs)
		

	def initialize(self,description_text='This is template', price=1):
		self.add_widget(BaseLabel(text=description_text, size_hint=(.7, .90)))
		self.add_widget(BaseButton(text=str(price), size_hint=(.3, .90)))
		




class ProgressBarLayout(BoxLayout):
	start = NumericProperty(0.0)
	current = NumericProperty(0.0)
	end = NumericProperty(0.0)
	tracked_attribute = StringProperty(None)
	_bar = ObjectProperty(None)
	initializable = False
	scrollable = False
	def __init__(self, start=0.0, end=1.0, bar_length=0, tracked_attribute=strings.DEFAULT, **kwargs):
		super(ProgressBarLayout, self).__init__(orientation='vertical', **kwargs)
		self.start, self.end = start, end
		self.tracked_attribute = tracked_attribute
		if bar_length==0:
			self.bind(width=self.update_bar)
		self._bar = Bar(pos=self.pos, bar_length=bar_length)
		self.add_widget(BaseLabel(text=str(self.tracked_attribute)))
		self.add_widget(self._bar)

	def update_bar(self, *args):
		self._bar._length=self.width * self.size_hint[0]

	def update(self, dt):
		attr = self.game_logic.get_attribute_by_string(self.tracked_attribute)
		if attr != self.current:
			self.current = attr
			self._bar.progress = max(min((self.current - self.start) / (self.end - self.start), 1.0), 0.0)

class MenuLayout(BoxLayout, BaseLayoutBehaviour):
	def __init__(self, **kwargs):
		super(MenuLayout, self).__init__(**kwargs)
		
	def initialize(self):
		self.add_widget(MenuButton(menu=strings.SCREEN_MAIN_GAMEPLAY, text=strings.descriptions[strings.SCREEN_MAIN_GAMEPLAY]))
		self.add_widget(MenuButton(menu=strings.SCREEN_UPGRADES, text=strings.descriptions[strings.SCREEN_UPGRADES]))
		self.add_widget(MenuButton(menu=strings.SCREEN_QUESTS, text=strings.descriptions[strings.SCREEN_QUESTS]))
		self.add_widget(MenuButton(menu=strings.SCREEN_OPTIONS, text=strings.descriptions[strings.SCREEN_OPTIONS]))
		self.add_widget(MenuButton(menu=strings.SCREEN_SHIP, text=strings.descriptions[strings.SCREEN_SHIP]))
		if self.root.debug_mode:
			self.add_widget(MenuButton(menu=strings.SCREEN_DEBUG, text=strings.descriptions[strings.SCREEN_DEBUG]))

	def add_widget(self, widget, **kwargs):
		widget.root = self.root
		widget.game_logic = self.game_logic
		super(BoxLayout, self).add_widget(widget, **kwargs)

class BasePopUpBehaviour(StackLayout):
	root = ObjectProperty(None)
	game_logic = ObjectProperty(None)
	initializable = True
	def close(self, *args):
		self.root_parent.unlock(self)
		self.root_parent.remove_widget(self)

	def add_widget(self, widget, **kwargs):
		widget.root = self.root
		widget.game_logic = self.game_logic
		super(BasePopUpBehaviour, self).add_widget(widget)

	def update(self, dt):
		for c in self.children:
			try:
				c.update(dt)
			except AttributeError:
				pass

class ConfirmationPopUp(BasePopUpBehaviour):
	def __init__(self, layout_fields={}, **kwargs):
		super(ConfirmationPopUp, self).__init__(**kwargs)
		self.layout_fields = layout_fields

	def initialize(self):
		self.add_widget(BaseLabel(text=self.layout_fields['message_field'], size_hint=(1, .5)))

class AttributeModifierPopUp(BasePopUpBehaviour):
	initial_value = NumericProperty(0)
	initial_value_2 = NumericProperty(0)
	def __init__(self, layout_fields={}, **kwargs):
		super(AttributeModifierPopUp, self).__init__(**kwargs)
		self.layout_fields = layout_fields

	def initialize(self):
		self.add_widget(BaseLabel(text=self.layout_fields['message_field'], size_hint=(1, .4)))
		self.add_widget(AttributeLabel(text=self.layout_fields['attribute_information_field_2'], attribute=self.layout_fields['attribute_variable_field_2'], size_hint=(1, .1)))
		self.add_widget(BaseButton(text="-", on_press=self.layout_fields['minus_action'], size_hint=(.1, .15)))
		self.add_widget(AttributeLabel(text=self.layout_fields['attribute_information_field'], attribute=self.layout_fields['attribute_variable_field'], size_hint=(.8, .15)))
		self.add_widget(BaseButton(text="+", on_press=self.layout_fields['plus_action'], size_hint=(.1, .15)))
		self.add_widget(BaseButton(text="OK", on_press=self.layout_fields['confirm_action'], size_hint=(.5, .2)))
		self.add_widget(BaseButton(text="Cancel", on_press=self.close, size_hint=(.5, .2)))

	def close(self, *args):
		
		super(AttributeModifierPopUp, self).close(*args)

class ListPopUp(BasePopUpBehaviour):
	pass

# one text field, data field, ok, cancel, do not show
class WarningPopUp(BasePopUpBehaviour):
	layout_fields = {}
	def __init__(self, layout_fields={}, **kwargs):
		super(WarningPopUp, self).__init__(**kwargs)
		self.layout_fields = layout_fields

	def initialize(self):
		self.add_widget(BaseLabel(text=self.layout_fields['message_field'], size_hint=(1, .5)))
		self.add_widget(AttributeLabel(text=self.layout_fields['attribute_information_field'], attribute=self.layout_fields['attribute_variable_field'], size_hint=(1, .1)))
		self.add_widget(BaseButton(text="OK", on_press=self.layout_fields['confirm_action'], size_hint=(.5, .2)))
		self.add_widget(BaseButton(text="Cancel", on_press=self.close, size_hint=(.5, .2)))
		#self.add_widget(CheckBoxItem())

# dumb test class
class PopUpMenu(BoxLayout, BaseLayoutBehaviour):
	def __init__(self, **kwargs):
		super(PopUpMenu, self).__init__(**kwargs)

	def initialize(self):
		self.add_widget(BaseButton(on_press=self.close))

	


