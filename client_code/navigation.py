import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users

from vault import vault
from homeanon import homeanon
from account import account
from datagen import datagen 

from scorecard import scorecard


home = None
def get_form():
  if home is None:
    raise Exception("You must set home form first.")

  return home
def go_vault():
  set_active_nav('vault')
  set_title("Vault")

  user = require_account()
  if not user:
    go_home()
    return
  
  form = get_form()
  form.load_component(vault())


def go_home():
  set_active_nav('home')
  set_title('')
  form = get_form()
  user = anvil.users.get_user()
  if user:
    form.load_component(vault())
  else:
    form.load_component(homeanon())

def go_datagen():
    print("Navigating to Datagen form...")  # Debugging print
    set_active_nav('datagen')
    set_title('DataGen')

    user = require_account()  # Check if the user is logged in
    if not user:
        go_home()  # Redirect to the home page if no user is logged in
        return

    form = get_form()
    print(f"Form found: {form}")  # Debugging print to ensure the form instance is correct
    form.column_panel_content.clear()  # Clear the content panel
    print("Cleared content panel")  # Debugging print
    form.load_component(datagen())  # Load the Datagen form
    print("Datagen Form Loaded")  # Debugging print


def go_scorecard():
  set_active_nav('scorecard')
  set_title("Scorecard")
  user = require_account()
  if not user:
    go_home()
    return

  
  form = get_form()
  form.load_component(scorecard())

def go_account():
  set_active_nav('account')
  set_title('Account')
  form = get_form()
  form.load_component(account())

def set_title(text):
  form = get_form()
  base_title = form.base_title
  if text:
    form.headline_1.text = base_title + ": " + text  
  else:
    form.headline_1.text = base_title
def set_active_nav(state):
  form = get_form()
  form.set_active_nav(state)

def set_account_state(self, user):
    self.link_account.visible = user is not None
    self.link_logout.visible = user is not None
    self.link_login.visible = user is None
    self.link_register.visible = user is None

def require_account():
    user = anvil.users.get_user()
    if user:
      return user
    
    user = anvil.users.login_with_form(allow_cancel=True)
    form = get_form()
    form.set_account_state(user)
    return user


  