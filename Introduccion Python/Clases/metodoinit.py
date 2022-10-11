class Usuario:

    def __init__(self, username, password):
        self.username = username
        self.password = password

user1 = Usuario('user', 'passworrd')
user2 = Usuario('user', 'passworrd')

print(user1.__dict__)
print(user2.__dict__)