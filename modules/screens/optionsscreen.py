class OptionsScreen(BaseScreen):
    def initialize(self):
        super(OptionsScreen, self).initialize()
        self.layout.add_widget(BaseLabel(text="Here's some cool options"))
        self.layout.add_widget(MenuLayout(pos_hint={'x':0, 'y':.92}))
        self.layout.add_widget(BaseButton(text='H', pos_hint={'x':.3, 'y':.05}, size_hint=(.4, .05), 
            on_press=partial(self.game_logic.display_popup, 
            popup_name="AttributeModifierPopUp", 
            layout_fields={
            'message_field':'Modify something', 
            'attribute_information_field':'This is info {0}',
            'attribute_variable_field':strings.RESOURCE_SHIP_COMMAND,
            'attribute_information_field_2':'This is info {0}',
            'attribute_variable_field_2':strings.RESOURCE_CREW,
            'minus_action':partial(self.game_logic.move_resource_by_amount, strings.RESOURCE_SHIP_COMMAND, strings.RESOURCE_CREW, 1),
            'plus_action':partial(self.game_logic.move_resource_by_amount, strings.RESOURCE_CREW, strings.RESOURCE_SHIP_COMMAND, 1),
            'confirm_action':self.game_logic.reset
            }, size_hint=(.8, .3), pos_hint={'x':.1, 'y':.3})
            ))