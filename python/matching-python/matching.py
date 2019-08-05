import webapp2
import jinja2
import os


the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

jack = "Jack"
# the handler section
class EnterInfoHandler(webapp2.RequestHandler):
    def get(self):  # for a get request
        welcome_template = the_jinja_env.get_template('template/matchPage.html')
        a_variable_dict = {
            "name": jack
            # "adjective": "amazing"
        }
        self.response.write(welcome_template.render(a_variable_dict))
#
# class ShowMemeHandler(webapp2.RequestHandler):
#     def get(self):
#         results_template = the_jinja_env.get_template('templates/results.html')
#         the_variable_dict = {
#             "line1": "If Cinderella's shoe was a perfect fit",
#             "line2": "Why did it fall off?",
#             "img_url": "https://upload.wikimedia.org/wikipedia/commons/f/ff/Deep_in_thought.jpg"
#         }
#         self.response.write(results_template.render(the_variable_dict))

app = webapp2.WSGIApplication([
    ('/', EnterInfoHandler)
    # ('/memeresult', ShowMemeHandler)
], debug=True)
