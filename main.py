"""`main` is the top level module for your Bottle application."""

# import the Bottle framework
from bottle import Bottle

# Create the Bottle WSGI application.
bottle = Bottle()
# We don't need to call run() since our application is embedded within                                                                                                         
# the App Engine WSGI application server. 

# Define an handler for the root URL of our application.
@bottle.route('/')
def hello():
  """Return a friendly HTTP greeting."""
  return 'Hello World'


# Define an handler for 404 errors.
@bottle.error(404)
def error_404(error):
  """Return a custom 404 error."""
  return 'Sorry, Nothing at this URL.'
