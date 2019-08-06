from google.appengine.ext import ndb

class CsusmUser(ndb.Model):
  first_name = ndb.StringProperty(required=True)
  last_name = ndb.StringProperty(required=False)
  email_address = ndb.StringProperty(required=False)
