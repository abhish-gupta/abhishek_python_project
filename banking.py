import sys
import random
import string

data = {
    1001: {'name': 'abhishek', 'add': 'jaipur', 'bal': 10000, 'ph_no': '9057182852', 'email': 'abhishek@gmail.com',
           'pas': 'abhishek'},
    1002: {'name': 'vikas', 'add': 'delhi', 'bal': 2000, 'ph_no': '8209065836', 'email': 'vikas@gmail.com',
           'pas': 'vikas123'},
    1003: {'name': 'yash', 'add': 'noida', 'bal': 5000, 'ph_no': '9887456158', 'email': 'yash@gmail.com',
           'pas': 'yash123'}
}


def main():
    print('welcome to the application')
    print('1.login\n2.signup\n3.exit')
    choice = int(input('Enter your choice:'))
    if choice == 1:
        login()
    elif choice == 2:
        signup()
    else:
        print('Thank you for using this service.')
        sys.exit()


def login():
    print('welcome to login page')
    acc = int(input('enter the acc num:'))
    if acc in data.keys():
        password = input('enter your password:')
        if data[acc]['pas'] == password:
            print('Loading......')

            print('logged in successfully:')
            print('1.debit\n2.credit\n3.check_balance\n4.exit')
            ch = int(input('Enter your choice:'))
            if ch == 1:
                debit(acc)
            elif ch == 2:
                credit(acc)
            elif ch == 3:
                check_balance(acc)
            elif ch == 4:
                sys.exit()
            else:
                print('invalid choice')
                main()
        else:
            print('invalid password please try again')
            login()
    else:
        print('your account number does not exist in our database')


def debit(db):
    amt = int(input('enter money to withdraw:'))
    if amt < data[db]['bal']:
        print('money is withdrawing........')
        data[db]['bal'] -= amt
    else:
        print('insufficient balance')
    print('remaining bal is:', data[db]['bal'])


def credit(cr):
    amt1 = int(input('enter money to be credited:'))
    print('money is credited!!')
    data[cr]['bal'] += amt1
    print('updated bal is:', data[cr]['bal'])


def check_balance(bal):
    print(data[bal]['bal'])


def signup():
    print('welcome to signup page')
    name = input('enter your name:')
    add = input('enter your address:')
    bal = int(input('enter your balance min balance 1000:'))
    if bal < 1000:
        print('entered amount is less than 1000')
        signup()
    mobile = input('enter your mobile:')
    email = input('enter your email:')
    acc_no = list(data.keys())[-1] + 1
    pas = ''
    password = string.ascii_letters + string.digits
    for var in range(8):
        pas = pas + random.choice(password)
    data[acc_no] = {'name': name, 'bal': bal, 'pas': pas, 'email': email, 'ph_no': mobile, 'add': add}
    print('Loading......')
    print(f'your account successfully created your acc_no is {acc_no} and password is {pas}.')
    for key, value in data.items():
        print(key, ' : ', value)


main()
