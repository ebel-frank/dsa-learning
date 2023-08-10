"""
    Question: As a senior backend engineer at Jovian, you are tasked with
    developing a fast in-memory data structure to manage profile information
    (username, name and email) for 100 million users. It should allow the
    following operations to be performed efficiently:
        1. Insert the profile information for a new user.
        2. Find the profile information of a user, given the username
        3. Update the profile information of a user, given their username
        4. List all the users of the platform, sorted by username
    Note: You can assume that usernames are unique.
"""


# We need to create a data structure which can store 100 million
# records and perform insertion, search, update and list operations efficiently.

class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email

    def __repr__(self):
        class_name = type(self).__name__
        return f"{class_name}(username='{self.username}', name='{self.name}', email='{self.email}')"

    def __str__(self):
        return self.__repr__()

    def introduce_yourself(self, guest_name):
        print(f"Hi {guest_name}, I'm {self.name}! Contact me at {self.email}.")


class UserDatabase:
    def __init__(self):
        self.users = []

    def insert(self, user):
        # Bruteforce approach
        i = 0
        while i < len(self.users):
            # Find the first username greater than the new user's username
            if self.users[i].username > user.username:
                break
            i += 1
        self.users.insert(i, user)

    def find(self, username):
        for user in self.users:
            if user.username == username:
                return user

    def update(self, user):
        target = self.find(user.username)
        target.name, target.email = user.name, user.email

    def list_all(self):
        return self.users


if __name__ == '__main__':
    database = UserDatabase()
    aakash = User("aakash", "Aakash Rai", "aakashrai@example.com")
    frank = User("frank", "Frank Mascott", "frankmascott@example.com")
    daniel = User("daniel", "Dannie Wind", "daniewind@example.com")
    chichi = User('chichi', "Chi Love", "chilove@example.com")
    database.insert(aakash)
    database.insert(frank)
    database.insert(daniel)
    print(database.find("frank"))
    database.update(User("frank", "Frank Hilton", "frankhilton@example.com"))
    print(database.find("frank"))

    database.insert(chichi)
    print(database.list_all())


