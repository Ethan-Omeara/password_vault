# Store username and password
USERNAME = "ethan"
PASSWORD = "password"

active = True

# Contains the main features and information about them
def exit():
    active = False

features = [
    {
        'description': "Exit the program",
        'run': exit
    }
]

def check_account():
    # Get username and password
    username_input = input("Input Username: ")
    password_input = input("Input Password: ")
    
    # Run the program if the username and password are correct
    if username_input == USERNAME and password_input == PASSWORD:
        return True
    else:
        return False

def menu_selection():
    # Explain menu
    print("Select function from the list below:")

    selectionString = ''
    for i, v in enumerate(features):
        selectionString += str(i + 1) + ' - ' + v['description'] + '\n'
    
    selection = input(selectionString)
    while not selection.isdigit() or int(selection) > len(features) or int(selection) == 0:
        print("Invalid input")
        selection = input(selectionString)
    return int(selection)-1
    
# Print program information
print('''Welcome to your password vault:
To use this program, simply type
your responses on the command line''')

if check_account():
    while active:
        selection = menu_selection()
        features[selection]['run']()

else:
    print("Incorrect username or password")
