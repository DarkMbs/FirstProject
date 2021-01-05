import pandas as pd
import numpy as np


names = []
balances = []
passwords = []

try:
    df = pd.read_csv('accounts.csv')
    for i in range(len(df['name'])):
        names.append(df['name'][i])
        balances.append(df['balance'][i])
        passwords.append(str(df['password'][i]))
except:
    with open('accounts.csv', 'w') as f:
        f.write(',name,balance,password')


def name_ser(name):
    found = False
    for i in range(len(names)):
        if names[i] == name:
            found = True
    return found


def acc_creation(name):
    names.append(name)
    balances.append(0)
    password_enter = input('Create a Password: ')
    passwords.append(password_enter)
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
        if name_ser(name_search) == True:
            print("Account Already excites!")
        else:
            acc_creation(name_search)
            print('Account created!')
    if opt == 2:
        name_search = input('Enter your login name: ')
        if name_ser(name_search) == True:
            password = input('Enter your password: ')
            for i in range(len(names)):
                if names[i] == name_search:
                    if password == passwords[i]:
                        print('Logged in!')


main_menu()
