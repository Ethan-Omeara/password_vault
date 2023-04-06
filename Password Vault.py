# Store username and password
USERNAME = "ethan"
PASSWORD = "password"

# Whether the program should continue running
active = True

# A class to contain the program features
class feature:
    def __init__(self, description, function):
        self.description = description
        self.run = function

def exit():
    print("Exiting Program")
    global active
    active = False

features = [
    feature("Exit Program", exit)
]

def check_account():
    '''Checks if username and password are correct'''
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

    # Print the description and number of every feature
    selectionString = ''
    for i, v in enumerate(features):
        selectionString += str(i + 1) + ' - ' + v.description + '\n'
    selectionString += "Input Selection: "
    
    # Get the user's input and ensure it is valid
    selection = input(selectionString)
    while not selection.isdigit() or int(selection) > len(features) or int(selection) == 0:
        print("Invalid input, please input a valid number from above")
        selection = input(selectionString)
    
    # Return the feature's index
    return int(selection)-1
    
# Print program information
print('''Welcome to your password vault:
To use this program, simply type
your responses on the command line''')

if check_account():
    while active:
        # Get player's feature selection
        selection = menu_selection()
        # Run feature
        features[selection].run()

else:
    print("Incorrect username or password")
