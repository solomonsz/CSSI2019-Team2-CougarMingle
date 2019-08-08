import webapp2
import jinja2
import os
from models import CsusmUser
from models import *
import models
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
    def post(self):
        welcome_template = the_jinja_env.get_template('templates/welcome.html')
        self.response.write(welcome_template.render())



class ShowCsusmUserHandler(webapp2.RequestHandler):
    def post(self):
        results_template = the_jinja_env.get_template('templates/usersPage.html')
        user_first_line = self.request.get('user-first-name')
        user_last_line = self.request.get('user-last-name')
        user_third_line = self.request.get('user-email-address')


        # GABY'S CODE START
        user_hobby_one = self.request.get('user_hobby_one')
        user_music_one = self.request.get('user_music_one')
        user_sports_one = self.request.get('user_sports_one')
        user_genre_one = self.request.get('user_genre_one')
        current_user_interests = CsusmUserInterests(
                                    hobby_one = user_hobby_one,
                                    music_one = user_music_one,
                                    sports_one = user_sports_one,
                                    genre_one = user_genre_one)
        current_user_interests.put()
        # GABY'S CODE END
        # IDK
        # count_obj = UserCount.query().fetch()[0]
        # current_count = count_obj.count
        # count_obj.count = current_count + 1
        # count_obj.put()

        current_user = CsusmUser(
                         first_name = user_first_line,
                         last_name = user_last_line,
                         email_address = user_third_line
                         # ,
                         # user_count = current_count
                         )
        current_user.put()
        the_variable_dict = {"line1": user_first_line,
                             "line2": user_last_line,
                             "line3": user_third_line
                             # GABY'S CODE START
                             ,
                             "hobbyOne": user_hobby_one,
                             "musicOne": user_music_one,
                             "sportsOne": user_sports_one,
                             "genreOne": user_genre_one
                             # GABY'S CODE END
                             }
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
