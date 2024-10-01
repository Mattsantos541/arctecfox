from ._anvil_designer import homeanonTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
from .. import navigation


class homeanon(homeanonTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def button_Register_click(self, **event_args):
    user = anvil.users.signup_with_form(allow_cancel=True)
    set_account_state(self, user) 
    navigation.go_vault() 






