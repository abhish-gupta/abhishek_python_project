import sys
import random
import string
import json


class Users:
    def write_file(self, data1, filename="data.json"):
        with open(filename, "w") as f:
            json.dump(data1, f, indent=4)

    def read_file(self):
        with open("data.json", "r") as f:
            temp = json.load(f)
        [print(x) for x in temp]

    def update_data(self, filename="data.json"):
        self.read_file()
        new_data = []
        with open(filename, "r") as f:
            temp = json.load(f)
        option = int(input("enter number which data you want to update:"))
        i = 0
        for entry in temp:
            if i == option:
                acc_no = entry["acc_no"]
                bal = entry["bal"]
                name = input('enter your new name:')
                add = input('enter your new add:')
                mobile = input('enter your new mobile:')
                password = input('enter your new password:')
                email = input('enter your new email:')
                new_data.append({'acc_no': acc_no, 'name': name, 'add': add, 'bal': bal, 'ph_no': mobile,
                                 'pas': password, 'email': email})
                i = i + 1
            else:
                new_data.append(entry)
                i = i + 1
        with open(filename, "w") as f:
            json.dump(new_data, f, indent=4)
        print("data updated successfully.")

    def delete_data(self, filename="data.json"):
        self.read_file()
        new_data = []
        with open(filename, "r") as f:
            temp = json.load(f)
        option = int(input("enter number which data you want to delete:"))
        i = 0
        for entry in temp:
            if i == option:
                i = i + 1
            else:
                new_data.append(entry)
                i = i + 1
        with open(filename, "w") as f:
            json.dump(new_data, f, indent=4)
        print("entry deleted successfully.")

    def main(self):
        print('welcome to the application')
        print('1.login\n2.signup\n3.print details\n4.delete entry\n5.update data\n6.exit')
        choice = int(input('Enter your choice:'))
        if choice == 1:
            self.login()
        elif choice == 2:
            self.signup()
        elif choice == 3:
            obj.read_file()
        elif choice == 4:
            obj.delete_data()
        elif choice == 5:
            obj.update_data()
        else:
            print('Thank you for using this service.')
            sys.exit()
        self.main()

    def login(self):
        flag = 0
        print('welcome to login page')
        acc = int(input('enter the acc num:'))
        with open("data.json", "r") as f:
            temp = json.load(f)
        for i in temp:
            if acc == i["acc_no"]:
                password = input('enter your password:')
                if i["pas"] == password:
                    print('Loading......')
                    print('logged in successfully:')
                    print('1.debit\n2.credit\n3.check_balance\n4.exit')
                    ch = int(input('Enter your choice:'))
                    if ch == 1:
                        self.debit(acc)
                    elif ch == 2:
                        self.credit(acc)
                    elif ch == 3:
                        self.check_balance(acc)
                    elif ch == 4:
                        print('Thank you for using this service.')
                        self.main()
                    else:
                        print('invalid choice')
                        self.main()
                else:
                    print('invalid password please try again')
                    self.login()
                flag = 0
                break
            else:
                flag = 1
        if flag == 1:
            print('your account number does not exist in our database')
        self.main()

    def debit(self, db):
        x = 0
        amt = int(input('enter money to be withdraw:'))
        with open("data.json", "r") as f:
            temp = json.load(f)
        for i in temp:
            if db == i["acc_no"]:
                if amt < i["bal"]:
                    print('money is withdrawing........')
                    x = i["bal"]
                    x -= amt
                    break
                else:
                    print('insufficient balance')

        print('remaining bal is:', x)
        self.main()

    def credit(self, cr):
        y = 0
        amt1 = int(input('enter money to be credited:'))
        print('money is credited!!')
        with open("data.json", "r") as f:
            temp = json.load(f)
        for i in temp:
            if cr == i["acc_no"]:
                y = i["bal"]
                y += amt1
        print('updated bal is:', y)
        self.main()

    def check_balance(self, bal):
        with open("data.json", "r") as f:
            temp = json.load(f)
        for i in temp:
            if bal == i["acc_no"]:
                print(i["bal"])
        self.main()

    def signup(self):
        print('welcome to signup page')
        with open("data.json") as json_file:
            temp = json.load(json_file)
            name = input('enter your name:')
            add = input('enter your add:')
            bal = int(input('enter your balance min balance 1000:'))
            if bal < 1000:
                print('entered amount is less than 1000')
                self.signup()
            mobile = input('enter your mobile:')
            email = input('enter your email:')
            acc_no = temp[-1].get("acc_no") + 1
            pas = ''
            password = string.ascii_letters + string.digits
            for var in range(8):
                pas = pas + random.choice(password)
            y = {"acc_no": acc_no, "name": name, "add": add, "bal": bal, "ph_no": mobile, "pas": pas, "email": email}
            temp.append(y)
            print('Loading......')
            print(f'your account successfully created your acc_no is {acc_no} and password is {pas}.')
            self.write_file(temp)
        self.main()


obj = Users()
obj.main()
