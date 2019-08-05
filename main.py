from models import CssiUser
class ShowMemeHandler(webapp2.RequestHandler):
    def post(self):

        user_cssiUser = CssiUser(
            user-email = self.request.get('user-email')
            user-first-name = self.request.get('first-name')
            user-second-name = self.request.get('second-name')

        )
