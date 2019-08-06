import webapp2
import jinja2
import os
from models import CsusmUser
from models import *
from google.appengine.ext import ndb
the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class HomePageHandler(webapp2.RequestHandler):
    def get(self):
        home_template = the_jinja_env.get_template('templates/homePage.html')
        self.response.write(home_template.render())

    def post(self):
        self.response.write("A post request to the HomePageHandler")


class EnterInfoHandler(webapp2.RequestHandler):
<<<<<<< HEAD
    # def get(self):  # for a get request
    #     welcome_template = the_jinja_env.get_template('templates/welcome.html')
    #     #a_variable_dict = {"title": "Sign Up"}
    #     self.response.write(welcome_template.render())
    def post(self):
        welcome_template = the_jinja_env.get_template('templates/welcome.html')
        self.response.write(welcome_template.render())
        q1 = self.request.get('question1')
        q2 = self.request.get('question2')
        q3 = self.request.get('question3')
        q4 = self.request.get('question4')
        squestion = questions(
                            question1 = q1,
                            question2 = q2,
                            question3 = q3,
                            question4 = q4)
        squestion.put()
# class SignUp(webapp2.RequestHandler):
#     def get(self):
#         q1 = self.request.get('question1')
#         q1 = self.request.get('question1')
#         q1 = self.request.get('question1')
#         q1 = self.request.get('question1')
#         squestion = questions(
#                          question1 = q1,
#                          question2 = q2,
#                          question3 = q3,
#                          question4 = q4)
=======
    # def get(self):  # for a get request
    #     welcome_template = the_jinja_env.get_template('templates/welcome.html')
    #     self.response.write(welcome_template.render())

    def post(self):
        welcome_template = the_jinja_env.get_template('templates/welcome.html')
        self.response.write(welcome_template.render())


>>>>>>> 379ec929deee37a9515cce5e9b03bce371c27c36

class ShowCsusmUserHandler(webapp2.RequestHandler):
    def post(self):
        results_template = the_jinja_env.get_template('templates/results.html')
        user_first_line = self.request.get('user-first-name')
        user_last_line = self.request.get('user-last-name')
        user_third_line = self.request.get('user-email-address')

        current_user = CsusmUser(
                         first_name = user_first_line,
                         last_name = user_last_line,
                         email_address = user_third_line)
        current_user.put()
        the_variable_dict = {"line1": user_first_line,
                             "line2": user_last_line,
                             "line3": user_third_line}
        self.response.write(results_template.render(the_variable_dict))

class ChatPage(webapp2.RequestHandler):
    def get(self):  # for a get request
        welcome_template = the_jinja_env.get_template('templates/matchPage.html')
        allusers = CsusmUser.query().fetch()
        a_variable_dict = {
            "name": name[2]
            # "adjective": "amazing"
        }
        self.response.write(welcome_template.render(a_variable_dict))

app = webapp2.WSGIApplication([
    ('/', HomePageHandler),
    ('/signUp', EnterInfoHandler),
    ('/userresult', ShowCsusmUserHandler),
    ('/matching',ChatPage),
], debug=True)
