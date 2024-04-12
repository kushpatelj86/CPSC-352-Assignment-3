passwordfile = "db.txt"


#part 1, prompt user to choose between login or create account

def main():
    return 0

def create_account():
    print("creating an account")
    username = input("username: ")

    #check if username already exists
    if ( is_username_exist( username) ):
        #report that username exists, and invalid
        pass
    else:
        # proceed with account creation
        pass
    return 0

def loginto_account():
    print("username and password: ")
    username = input("username: ")
    #check if username already exists
    if ( is_username_exist( username) ):
        #proceed for login
        pass
    else:
        #report that username is not exist
        pass

    return 0

def is_username_exist( username = ""):



    is_exist = False
    return is_exist

def part1():
    print("""Would you like to:
    (1): create an account
    (2): login into an existing account""")
    user_input = input()

    if user_input == "1":
        create_account()
    elif user_input == "2":
        loginto_account()
part1()






  
