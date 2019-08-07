from google.appengine.ext import ndb



class CsusmUser(ndb.Model):
    first_name = ndb.StringProperty(required=True)
    last_name = ndb.StringProperty(required=False)
    email_address = ndb.StringProperty(required=False)
    user_count = ndb.IntegerProperty(default=0)

# # <<<<<<< HEAD
# # # COMMENT/
# =======
# # <<<<<<< HEAD
# #
# # class questions(ndb.Model):
# #   question1 = ndb.StringProperty(required=True)
# #   question2 = ndb.StringProperty(required=True)
# #   question3 = ndb.StringProperty(required=True)
# #   question4 = ndb.StringProperty(required=True)
# # =======
# # COMMENT
# >>>>>>> 6a8de0514cb5fb1899fc22838bfdb3e9c00f6f16
# # class questions(ndb.Model):
# #     question1 = ndb.StringProperty(required=True)
# #     question2 = ndb.StringProperty(required=True)
# #     question3 = ndb.StringProperty(required=True)
# #     question4 = ndb.StringProperty(required=True)
# # COMMENT

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
