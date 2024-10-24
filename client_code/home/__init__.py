from ._anvil_designer import homeTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
from .. import navigation  # Ensure this import statement is correct


class home(homeTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        # Set up initial UI state based on user status
        self.update_ui_based_on_user()
        # Any code you write here will run before the form opens.
        self.base_title = self.headline_1.text
        navigation.home = self
        user = anvil.users.get_user()
        print("Current user:", user)
        self.set_account_state(user)

        
        navigation.go_home()

        # Moved the user welcome message logic inside a method to ensure it's called correctly
        #self.update_welcome_message(user)
    def form_show(self, **event_args):
        # Refresh UI state every time the form is shown
        self.update_ui_based_on_user()

    def update_ui_based_on_user(self):
        """Updates UI components based on the user's login state."""
        user = anvil.users.get_user()
        if user:
            self.link_account.text = f"Welcome {user['email']}"
            self.link_logout.visible = True
            self.link_login.visible = False
            self.link_register.visible = False
        else:
            self.link_account.text = "Welcome Guest"
            self.link_logout.visible = False
            self.link_login.visible = True
            self.link_register.visible = True


    def link_account_click(self, **event_args):
        navigation.go_account()

    def link_home_click(self, **event_args):
        navigation.go_home()

    def link_vault_click(self, **event_args):
        navigation.go_vault()

    def link_datagen_click(self, **event_args):
        navigation.go_datagen()

    def link_scorecard_click(self, **event_args):
        navigation.go_scorecard()

    def link_register_click(self, **event_args):
        user = anvil.users.signup_with_form(allow_cancel=True)
        self.set_account_state(user)
        navigation.go_vault()

    def link_login_click(self, **event_args):
        user = anvil.users.login_with_form(allow_cancel=True)
        self.set_account_state(user)
        navigation.go_vault()

    def link_logout_click(self, **event_args):
        anvil.users.logout()
        self.set_account_state(None)
        navigation.go_home()

    def load_component(self, cmpt):
      print("Clearing content panel and loading new component...")  # Debugging print
      self.column_panel_content.clear()
      self.column_panel_content.add_component(cmpt)
      print("Component loaded into content panel.")  # Debugging print


    def set_active_nav(self, state):
        self.link_home.role = 'selected' if state == 'home' else None
        self.link_vault.role = 'selected' if state == 'vault' else None
        self.link_datagen.role = 'selected' if state == 'datagen' else None
        self.link_scorecard.role = 'selected' if state == 'scorecard' else None

    def set_account_state(self, user):
        self.link_account.visible = user is not None
        self.link_logout.visible = user is not None
        self.link_login.visible = user is None
        self.link_register.visible = user is None
        # update welcome message 
        self.update_ui_based_on_user()
