names = input("What are ur names: ")

for name in names.strip().replace(".", "").split(" "):
    match name.strip().lower():
        case "akachukwu":
            print(name, "is my middle name.")
        case "chukwumam":
            print(name,"is my first name.")
        case "david":
            print(name, "is my last Name.")
        case "mimi"|"ada"|"makua"|"zizi":
            print(name, "is my sister's name.")
        case "somto"|"divine":
            print(name, "is my brother's name.")
        case "betson"|"amaka":
            print(name, "is my parent's name.")
        case _:
            print(name, "doesn't belong to any memeber of my nuclear family.")
