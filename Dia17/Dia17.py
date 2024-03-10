#Crear una clase
class User: #Utiliza PascalCase
    def __init__(self, user_id, user_name): #Puedes agregar cuantos atributos necesites
        self.id=user_id
        self.name=user_name
        self.followers=0 #Atributo con valor por defecto (se puede modificar más adelante)
        self.following= 0
    def newFollower(self, user):
        user.followers+=1
        self.following+=1
        

user1=User(1, "Carlos") #Inicializa con el parentesis la creacion del objeto
user2=User(4, "Cristian")


user2.newFollower(user1)
print(user1.followers, user1.following)
print(user2.followers, user2.following)