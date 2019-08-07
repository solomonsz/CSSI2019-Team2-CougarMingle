from google.appengine.ext import ndb

class CsusmUser(ndb.Model):
  first_name = ndb.StringProperty(required=True)
  last_name = ndb.StringProperty(required=False)
  email_address = ndb.StringProperty(required=False)

# COMMENT
# class questions(ndb.Model):
#     question1 = ndb.StringProperty(required=True)
#     question2 = ndb.StringProperty(required=True)
#     question3 = ndb.StringProperty(required=True)
#     question4 = ndb.StringProperty(required=True)
# COMMENT

# GABY'S CODE START
class CsusmUserInterests(ndb.Model):
    hobby_one = ndb.StringProperty(required=True)
    music_one = ndb.StringProperty(required=True)
    sports_one = ndb.StringProperty(required=True)
    genre_one = ndb.StringProperty(required=True)
# GABY'S CODE END
