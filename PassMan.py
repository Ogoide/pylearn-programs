# Protoype password manager, to apply dictionaries and file managing with pickle
import pickle, os, time

try:
    # Loading data from a file
    passwords_file = open('passwordsDump', 'rb')
    passwords = pickle.load(passwords_file)
    passwords_file.close()
except:
    passwords = {}

while True:
    os.system('cls')
    print('Choose an option:\n[1] Login\n[2] Register new user\n[3] List registered users\n[4] Exit')
    choice = input('Select your action:\t')
    if choice == '1':
        os.system('cls')
        user = input('Enter your username:\n')
        password = input('Enter your password:\n')
        if user in passwords.keys():
            if password == passwords[user]:
                print('Login successful!')
                while True:
                    time.sleep(1)
                    os.system('cls')
                    print('Choose an option:\n[1] Delete account\n[2] Exit')
                    login_action = input('Select your action:\n')
                    if login_action == '1':
                        del passwords[user]
                        print('Account successfully deleted.\nLogging out...')
                        time.sleep(1)
                        break
                    elif login_action == '2':
                        print('Logging out...')
                        time.sleep(1)
                        break
                    else:
                        print('Sorry, I couldn\'t understand your choice!')
                        time.sleep(1)
            elif user in passwords.keys():
                print('Your password doesn\'t match your username.')
                time.sleep(1)
        else:
            print('User not existent.')
            time.sleep(1)
    elif choice == '2':
        os.system('cls')
        new_user = input('Create a new username:\n')
        if new_user in passwords.keys():
            print('That username already exists.')
            time.sleep(1)
        else:
            new_password = input('Create a new password:\n')
            password_confirm = input('Please confirm your password:\n')
            if new_password == password_confirm:
                print('Password confirmed!')
                time.sleep(1)
                passwords.setdefault(new_user, new_password)
            else:
                print('The passwords don\'t match.')
                time.sleep(1)
    elif choice == '3':
        os.system('cls')
        print('Registered users:')
        for u in passwords.keys():
            print(f'- {u}')
        time.sleep(1)
    elif choice == '4':
        print('Exiting...')
        time.sleep(1)
        break
    else:
        print('Sorry, I couldn\'t understand your choice!')
        time.sleep(1)

# Storing data on a file
passwords_file = open('passwordsDump', 'wb')
pickle.dump(passwords, passwords_file)
passwords_file.close()