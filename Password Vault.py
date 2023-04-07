# Store username and password
USERNAME = "ethan"
PASSWORD = "password"

# Whether the program should continue running
active = True

# Accounts
accounts = [
    ["Netflix", "Password1"],
    ["YouTube", "Password2"],
    ["GitHub", "Password3"]
]

def get_input(array, desc_index, description = ''):
    print(description)
    # Print and number descriptions in array
    selection_string = ''
    for i, v in enumerate(array):
        # Check if the object in the array is a list or class
        # as classes have a different method of getting attribute
        if isinstance(v, list):
            selection_string += '{} - {}\n'.format(i + 1, v[desc_index])
        else:
            selection_string += '{} - {}\n'.format(i + 1, getattr(v, desc_index))
    selection_string += "Input Selection From Above: "
    
    # Get users' input and check if valid
    selection = input(selection_string)
    while not selection.isdigit() or int(selection) > len(array) or int(selection) == 0:
        selection = input("Invalid input, please input a valid number from above: ")
    
    # Return index of selection
    return int(selection) - 1

def validate_password(password):
    has_digits = any(char.isdigit() for char in password)
    has_letters = any(char.isalpha() for char in password)
    has_length = len(password) >= 8
    return has_digits and has_letters and has_length

# A class to contain the program features
class feature:
    def __init__(self, description, function):
        self.description = description
        self.run = function

def find_password():
    # Get account
    selection = get_input(accounts, 0, 'Accounts:')
    
    print('Password: ' + accounts[selection][1])
    return

def add_account():
    # Get account name
    account_name = input("Input New Account Name: ")
    # End if account already exists
    for v in accounts:
        if v[0] == account_name:
            print("Account Already Exists")
            return
    
    # Get account password
    account_password = input("Input New Account Password: ")
    # Check if the length is 8 or over and has digits and letters
    while validate_password(account_password) == False:
        print("Password Must Have A Minimum Length of 8, And Contain At Least 1 Letter and 1 Digit")
        account_password = input("Input New Account Password: ")
    
    # Add password to vault
    print("Password Added To Vault")
    accounts.append([account_name, account_password])

def change_password():
    # Get account
    selection = get_input(accounts, 0, 'Account To Change:')

    account_password = input("Input New Password: ")
    # Check if the length is 8 or over and has digits and letters
    while validate_password(account_password) == False:
        print("Password Must Have A Minimum Length of 8, And Contain At Least 1 Letter and 1 Digit")
        account_password = input("Input New Account Password: ")
    
    print("Password Updated")
    accounts[selection][1] = account_password

def remove_account():
    # Get account
    selection = get_input(accounts, 0, 'Account To Delete:')
    del accounts[selection]
    print("Account Deleted")

def exit():
    print("Exiting Program")
    global active
    active = False

features = [
    feature("Find Password", find_password),
    feature("Add Account", add_account),
    feature("Change Password", change_password),
    feature("Remove Account", remove_account),
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
    
# Print program information
print('''Welcome to your password vault:
To use this program, simply type
your responses on the command line''')

if check_account():
    while active:
        # Get player's feature selection
        selection = get_input(features, 'description', "Select feature from the list below:")
        # Run feature
        features[selection].run()
else:
    print("Incorrect username or password")
