# Step 1: Access Code Validation

#1.Create the ACCESS_CODE variable
ACCESS_CODE = "CIT"

#2.Define the function and set the condition
def check_access_code(user_input):
    if user_input == ACCESS_CODE:
        return True
    else:
        return False

# 3.Ask the user for input to compare to ACCESS_CODE
user_input = input("Enter the access code: ")

# 4. Call the function and print the result
if check_access_code(user_input):
    print("Access approved. Welcome!")
else:
    print("Access denied. Invalid access code")
    

# Step 2: User Login Authentication

login_credentials = {"alice": "123","bob": "abc","david": "999"}

def verify_login(credentials, username, password):
    if username in credentials:
        if credentials[username] == password:
            return True
        else:
            return False
    else:
        return False

username = input("Enter username: ")
password = input("Enter password: ")

if verify_login(login_credentials, username, password):
    print("Login successful")
else:
    print("Login failed")

