from google.appengine.ext import ndb

class CsusmUser(ndb.Model):
    first_name = ndb.StringProperty(required=True)
    last_name = ndb.StringProperty(required=False)
    email_address = ndb.StringProperty(required=False)
    user_count = ndb.IntegerProperty(default=0)


# GABY'S CODE START
class CsusmUserInterests(ndb.Model):
    hobby_one = ndb.StringProperty(required=True)
    music_one = ndb.StringProperty(required=True)
    sports_one = ndb.StringProperty(required=True)
    genre_one = ndb.StringProperty(required=True)
# GABY'S CODE END

class UserCount(ndb.Model):
    count = ndb.IntegerProperty(default=0)

    def increment(self):
        self.count += 1

# count = UserCount()
# count.put()
