class User:
    nextUserId = 1 #zmienna statyczna/klasowa

    def __init__(self, name=""):
        self.name = name
        self.id = User.nextUserId
        User.nextUserId += 1