def check_password(password: str):
    with open('C:\Projects\Python_Starter_Projects\python_starter_projects\password_checker\passwords.txt', 'r') as file:
        common_passwords: list[str] = file.read().splitlines()

    for i, common_password in enumerate(common_passwords, start=1):
        if password == common_password:
            print(f'{password}: False (#{i})')
            return 

    print(f'{password}: True (Unique)')

def main():
    user_password: str = input('Enter a password: ')
    check_password(user_password)

if __name__ == '__main__':
    main()
