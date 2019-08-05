from google.appengine.ext import ndb

class CssiUser(ndb.Model):
  email = ndb.StringProperty(indexed=True)
  first_name = ndb.StringProperty()
  last_name = ndb.StringProperty()
