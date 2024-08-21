master_pwd = input("enter master password: ")

# def main():
#         add()

def view():
    pass
def add():
    name = input("account name: ")
    pwd = input("password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + pwd)

while True:
    mode = input("add new pass | view saved passwords | (add) (view), press q to quit \n" ).lower
    if mode == "q":
        break

    if mode == "add":
        add()
    elif mode == "view":
        view()

    else:
        # print("invalid mode")
        pass
