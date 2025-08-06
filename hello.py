import config
def say_hello(name):
    print(f"Hello, {name}! Welcome to {config.APP_NAME}!")

def greet_user():
    user_name = input("Please enter your name: ")
    say_hello(user_name)
    
if __name__ == "__main__":
    greet_user()