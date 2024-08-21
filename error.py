try:
    the_file = open('reference.txt')
    print(the_file.name)
except Exception:
    print("Soryy, this fie cannot be found here")
