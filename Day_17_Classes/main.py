# class
class User:
    def __init__(self, user_id, username):
        # initialize attributes
        print("new user is being created...")
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        # increase the followers of the user our object is going to follow
        user.followers += 1
        # increase the following count of our object
        self.following += 1

user_1 = User("001", "angela")
print(user_1.id)
print(user_1.username)

user_2 = User("002", "jack")
user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)

# user_1 = User()
# user_1.id = "001"
# user_1.username = "angela"
# print(user_1.username)

# user_2 = User()
# user_2.id = "002"
# user_2.username = "jack"

# def function():
#     pass
#
# print("hello")