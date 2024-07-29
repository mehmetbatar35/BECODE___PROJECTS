import json
import os

class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email


class UserRepository:
    def __init__(self):
        self.users = []
        self.isLoggedIn = False
        self.currentUser = {}

        #load users from .json file
        self.loadUsers()

    def loadUsers(self):
        if os.path.exists('users.json'):
            with open('users.json', 'r', encoding='utf-8') as file:
                users = json.load(file)
                for user in users:
                    newUser = User(username = user['username'], password = user['password'], email = user['email'])
                    self.users.append(newUser)
                    # print(user['username'])
                    # print(user)
            print(self.users)


    def register(self, user: User):
        self.users.append(user)
        self.savetoFile()
        print("New user is created.")

    def savetoFile(self):
        
        my_list = []

        for user in self.users:
            my_list.append(user.__dict__)
            # my_list.append(json.dumps(user.__dict__))    
        with open("users.json", 'w') as file:
            json.dump(my_list, file, indent = 4)


    def login(self, username, password):

        for user in self.users:
            if user.username == username and user.password == password:
                self.isLoggedIn = True
                self.currentUser = user
                print("Login is done.")
                break
    
    def logout(self):
        self.isLoggedIn = False
        self.currentUser = {}
        print('Logout is done.')
        
    def identity(self):
        if self.isLoggedIn :
            print(f"user: {self.currentUser.username}")
        else:
            print("Not Log in.")


repository = UserRepository()

while True:
    print("Menu".center(50, '*'))            
    chooice = input('1- Register\n2- Login\n3- Logout\n4- identity\n5- Exit\nChooice: ')
    
    if chooice == '5':
        break
    else:
        if chooice == '1':
            username = input("username: ")
            password = input("password: ")
            email = input("email: ")

            user = User(username = username, password = password, email = email)
            repository.register(user)


        elif chooice == '2':
            if repository.isLoggedIn:
                print("Already Logged in")
            else:            
                username = input("username: ")
                password = input("password: ")
                repository.login(username, password)
        elif chooice == '3':
            repository.logout()
        elif chooice == '4':
            repository.identity()
        else:
            print('Wrong chooice')
            