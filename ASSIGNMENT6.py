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


#Step 2.1: “User Not Found” and Step 2.2: Limit Login Attempts 

login_credentials = {"alice": "123","bob": "abc","david": "999"}

# Step 2.1
def verify_login(credentials, username, password):
    if username not in credentials:
        print("User not found")
        return False
    elif credentials[username] != password:
        print("Incorrect password")
        return False
    else:
        print("Login Successful")
        return True

# Step 2.2
attempts = 0
while attempts < 3:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if verify_login(login_credentials, username, password):
        break  # stop if login successful
    else:
        attempts += 1
        if attempts == 3:
            print("Too many failed attempts. Access blocked")


#Step 3: Role-Based Authorization

user_accounts = {
    "alice": {"password": "1234", "role": "admin"},
    "bob": {"password": "abcd", "role": "user"},
    "david": {"password": "9999", "role": "user"}
}

def authorize_user(accounts, username, password):
    if username in accounts:
        if accounts[username]["password"] == password:
            return accounts[username]["role"]
        else:
            return None 
    else:
        return None 

username = input("Enter username: ")
password = input("Enter password: ")

role = authorize_user(user_accounts, username, password)

if role is None:
    print("Authentication failed. Access not authorized")
else:
    print("Authentication successful. Role assigned:" + role )

# Step 3.1: Admin Password Reset

    if role == "admin":
        print("Admin access granted")
        target_user = input("Enter the username of the account to reset: ")

        if target_user in user_accounts:
            new_password = input("New password for " +target_user+ ":")
            user_accounts[target_user]["password"] = new_password
            print("Password successfully updated for user:" + target_user )
        else:
            print("User not found. Cannot reset password.")






