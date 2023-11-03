
admins = ["Walid", "Karem", "Ahmed", "Mohamed"]
userName = input("Enter your username please: ").strip().capitalize()

if userName in admins:
    print(f"Hello {userName}, Welcome back")
    option = input('Enter "Delete" or "Update" the username: ').strip().capitalize()

    if option == "Update":
        newUserName = input("Enter the new username please: ").strip().capitalize()
        admins[admins.index(userName)] = newUserName
        print("Name Updated.")

    elif option == "Delete":
        admins.remove(userName)
        print("User Deleted.")
    else:
        print("Please Enter a right option")

else:
    print("Sorry, You're not an Admin")