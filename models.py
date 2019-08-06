from google.appengine.ext import ndb

class CsusmUser(ndb.Model):
  user_first_name = ndb.StringProperty()
  user_second_name = ndb.StringProperty()
  u_user_email = ndb.StringProperty(indexed=True)
