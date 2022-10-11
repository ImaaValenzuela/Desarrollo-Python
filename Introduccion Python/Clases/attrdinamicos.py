class Usuario:
    username = 'Enlighted'
    email =''

Usuario.email = 'mimail@example.com'

user1 = Usuario()
user1.password = '1234'

print(user1.username)

print(id(user1.username))
print(id(Usuario.username))

print(user1.__dict__)