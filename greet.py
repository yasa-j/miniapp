import datetime

def greet(name):
    now = datetime.datetime.now()
    return f"Hello, {name}! Current time is {now:%Y-%m-%d %H:%M:%S}"

if __name__ == "__main__":
    user = input("Enter your name: ")
    print(greet(user))