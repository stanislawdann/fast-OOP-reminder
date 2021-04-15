from user import User

users = [User() for _ in range(10)]

for user in users:
    print(user.id)

print("next: ",User.nextUserId)