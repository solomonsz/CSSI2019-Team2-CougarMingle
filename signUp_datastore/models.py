from google.appengine.ext import ndb

class CsusmUser(ndb.Model):
  first_name = ndb.StringProperty(required=True)
  last_name = ndb.StringProperty(required=False)
  email_address = ndb.StringProperty(required=False)

class questions(ndb.Model):
    question1 = ndb.StringProperty(required=True)
    question2 = ndb.StringProperty(required=True)
    question3 = ndb.StringProperty(required=True)
    question4 = ndb.StringProperty(required=True)
