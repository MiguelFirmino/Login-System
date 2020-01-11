data_text = []
first_names = []
last_names = []
emails = []
passwords = []

def user_choice():
    print('Hello user, create an account or login to an existing one.')
    choice = input('Insert "1" if you wish to create an account or "2" if you wish to login: ')
    print('\r')
    if choice == '1':
        create_account()
        user_choice()
    else:
        login_account()
        user_choice()

def register_info():
    with open('Login_Data.txt', 'r') as login_data:
        global data_text, first_names, last_names, emails, passwords
        data_text = login_data.readlines()
        for i in data_text:
            data_text[data_text.index(i)] = i.strip()
        emails = (data_text[2::4])

def create_account():
    with open('Login_Data.txt', 'a') as login_data:
        first_name = input('First name: ')
        last_name = input('Last name: ')
        email = input('Insert your Email adress: ')
        while email in emails:
            print('That email is already registered')
            email = input('Insert another Email adress: ')
        password = input('Create a password: ')
        passwordc = input('Confirm your password: ')
        info = [first_name, last_name, email, password]
        while passwordc != password:
            print('The passwords do not match.')
            passwordc = input('Reinsert your password: ')
        for i in info:
            login_data.write(i)
            login_data.write('\n')
    print('Nice! Your account was registered.')
    print('\r')
    register_info()

def login_account():
    register_info()
    with open('Login_Data.txt', 'r'):
        login_email = input('Email: ')
        while login_email not in emails:
            print('Invalid Email')
            login_email = input('Reinsert your Email: ')
        login_password = input('Password: ')
        while login_password != data_text[data_text.index(login_email) + 1]:
            print('Invalid password')
            login_password = input('Reinsert your password: ')
        print('Hello {} {}, welcome back!'.format(data_text[data_text.index(login_email) - 2], data_text[data_text.index(login_email) - 1]))
        print('\r')
user_choice()