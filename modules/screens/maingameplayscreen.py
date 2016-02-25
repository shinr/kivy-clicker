from modules.screens.basescreen import BaseScreen
from ui.buttons.clickbutton import ClickButton
from ui.labels.attributelabel import AttributeLabel
import utils.utils as utilities

class MainGameplayScreen(BaseScreen):
    def on_starclicker_reset_event(self, *args):
            pass
            
    def initialize(self):
        self.register_event_type('on_starclicker_reset_event')
        super(MainGameplayScreen, self).initialize()
        self.layout.add_widget(AttributeLabel(
            text='Science {0}', 
            pos_hint={'x':.5, 'y':.7}, 
            size_hint=(.20, .05))) 
        self.layout.add_widget(ClickButton( 
            pos_hint={'x':.3, 'y':.15}, 
            size_hint=(.4, utilities.convert_from_width_to_height(.4))))
        """
        self.layout.add_widget(MenuLayout(
            pos_hint={'x':0, 'y':.92}))
        self.layout.add_widget(ProgressBarLayout(
            0.0, 
            10.0, 
            tracked_attribute=strings.RESOURCE_SCIENCE, 
            pos_hint={'x':.1, 'y':.52}, 
            size_hint=(.8, .05)))       
        self.layout.add_widget(BaseButton(
            text='Warp!', 
            pos_hint={'x':.3, 'y':.05}, 
            size_hint=(.4, .05), 
            on_press=partial(self.game_logic.display_popup, 
                popup_name="WarningPopUp", 
                layout_fields={
                'confirm_action':self.game_logic.reset,
                'attribute_variable_field':strings.RESOURCE_SCIENCE,
                'message_field':'Are you sure?',
                'attribute_information_field':'Attribute {0}',
                'confirm_function':self.game_logic.reset}, 
                size_hint=(.8, .3), 
                pos_hint={'x':.1, 'y':.3})))
        """

        
