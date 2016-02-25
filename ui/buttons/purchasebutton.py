class PurchaseButton(BaseButton):
	upgrade = ObjectProperty(0)

	def button_pressed(self, **kwargs):
		self.dispatch("starclicker_purchasebutton_pressed")