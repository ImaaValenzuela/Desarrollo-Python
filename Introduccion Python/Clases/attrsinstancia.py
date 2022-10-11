class Usuario:
    username = 'Enlighted'
    email =''

Usuario.email = 'mimail@example.com'

user1 = Usuario()

print(user1.username)

print(id(user1.username))
print(id(Usuario.username))

print(user1.__dict__)