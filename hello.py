import datetime 

class config:
    APP_NAME = "MyApp"

def say_hello(name):
    print(f"Hello, {name}! Welcome to {config.APP_NAME}!")

def sqy_hello(name):
    now = datetime.datetime.now()
    print(f"Hello again,{name} from {config.APP_NAME}!")
    print(f"Today is {now.strftime('%Y-%m-%d')}")

def greet_user():
    user_name = input("Please enter your name: ")
    say_hello(user_name)
    
if __name__ == "__main__":
    greet_user()