import pandas as pd
from cryptography.fernet import Fernet
import numpy as np


try:
    file = open('pwkey', 'r')
    key = file.read()
    file.close()
except:
    key = Fernet.generate_key()
    file = open('pwkey', 'wb')
    file.write(key)
    file.close()


names = []
balances = []
passwords = []

try:
    df = pd.read_csv('accounts.csv')
    for i in range(len(df['name'])):
        names.append(df['name'][i])
        balances.append(df['balance'][i])
        passwords.append(df['password'][i])
except:
    f = open('accounts.csv', 'w')
    f.write(',name,balance,password')


def name_ser(name):
    # Check if element is in list
    if name in names:
        # Return index of element
        return names.index(name)
    else:
        # Name was not found in the list
        return -1


def acc_creation(name):
    names.append(name)
    balances.append(0)
    password_enter = input('Create a Password: ')
    encry_p = password_enter.encode()
    f = Fernet(key)

    encry_pass = f.encrypt(encry_p)
    encry_pass = encry_pass.decode('ascii')
    passwords.append(encry_pass)
    new_df = pd.DataFrame(np.column_stack([names, balances, passwords]),
                          columns=['name', 'balance', 'password'])
    new_df.to_csv('accounts.csv', encoding='utf-8', sep=',',
                  header=True, na_rep=0, index=True)


def bal_check(name):
    for i in range(len(names)):
        if df['name'][i] == name:
            print(name + ' your balance is $' +
                  str(df['balance'][i]))
            break
        else:
            pass


def main_menu():
    print('Welcome!\nPlease Choose from the following options...')
    print('1: Create an account\n2: Login ')
    opt = int(input('Enter Your Choice: '))
    if opt == 1:
        name_search = input('Enter Name... ')
        if name_search in names:
            print("Account Already exists!")
        else:
            acc_creation(name_search)
            print('Account created!')

    if opt == 2:
        name_search = input('Enter your login name: ')
        found = name_ser(name_search)
        if found != -1:
            password = input('Enter your password: ')
            dec_pass = bytes(passwords[found], 'utf-8')
            f = Fernet(key)
            decrypted = f.decrypt(dec_pass)
            decrypted = decrypted.decode()
            if password == decrypted:
                print('Logged in!')

            else:
                print('Invalid username or password')


op = 2
while op != 0:
    main_menu()
    op = int(input('Do You want to exit the program?\n0:Yes \n1:No\n'))
