import webapp2
from models import CsusmUser

class MainHandler(webapp2.RequestHandler):
    def get(self):
        current_user_email = self.request.get('user-email')
        current_user_first_name = self.request.get('first-name')
        current_user_second_name = self.request.get('second-name')

        user_csusmUser = CssiUser(
            user_first_name = current_user_first_name,
            user_second_name = current_user_second_name,
            u_user_email = current_user_email
        )

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
