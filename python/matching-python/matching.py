import webapp2
import jinja2
import os
from models import *
from google.appengine.ext import ndb
the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


# the handler section
class ChatPage(webapp2.RequestHandler):
    def get(self):  # for a get request
        welcome_template = the_jinja_env.get_template('template/matchPage.html')
        name = first_name.query().fetch()
        a_variable_dict = {
            "name": name
            # "adjective": "amazing"
        }
        self.response.write(welcome_template.render(a_variable_dict))



app = webapp2.WSGIApplication([
    ('/',ChatPage)
    # ('/memeresult', ShowMemeHandler)
], debug=True)
