def genesis():
    while True:
        print('----------------------------------------------------------------------------------------------')
        options = int(input("Please press \n1 to Login \nOR \n2 to Close:"))
        if options == 1:
            username = input("Please enter your DESIGNATED USERNAME:")
            password = input("Please enter your SECRET PASSWORD:")
            with open('staff.txt')as d:
                databank = d.readlines()
                d.close()
            usernames = databank[::4]
            user_names_list=[]
            for i in range(len(usernames)):
                user_names_list.append(usernames[i].strip("\n"))
            #print(user_names_list)                                                             ##(test script)
            passwords = databank[1::4]
            passkeys=[]
            for i in range(len(passwords)):
                passkeys.append(passwords[i].strip("\n"))
            #print(passkeys)                                                                            ##(test script)
            if username in user_names_list and password in passkeys:
                print("____-----WELCOME TO SN BANK-----_____")
                with open('sessions.txt', 'w') as f:
                    f.write('{}\n'.format(username))
                    f.write('{}\n'.format(password))
                show_account_options()
            else:
                print("ERROR: please enter  valid credentials")
        elif options == 2:
            print("... Closing App ...")
            break
        else:
            print("------------Please Try again---------------")

def get_account_no(n):
  from random import randint
  start = 10**(n-1)
  end = (10**n)-1
  return randint(start,end)

def check_file_exist(filename):
  import os
  if os.path.exists(filename):
    return True


def fetch_account_details(acctno):
  with open('customer.txt', 'r') as f:
      read_data = f.readlines()
      f.close()
      if acctno == read_data[4].strip('\n'):
        return read_data
      else:print('please enter a proper account number')


def show_account_options():
    try:
        account_options = int(input("Please select your preferred option option \n1. Create new bank account \n2. Check Account Details \n3. Logout  "))
        if account_options == 1:
            # get user account details for creating account
            accountName = input("Please enter the Account name")
            openingBalance = input("Please enter the Opening balance")
            accountType = input("Please enter the Account Type")
            accountEmail = input("Please enter the Account Email")
            accountNumber = get_account_no(10)
            accountDetails = [accountName, openingBalance, accountType, accountEmail, accountNumber]
            # Store details in customer file
            with open('customer.txt', 'w') as writer:
                for item in accountDetails:
                    writer.write("{}\n".format(item))
            print('Your account has been created with account number {}'.format(accountNumber))
            show_account_options( )

            print("Account created")
        elif account_options == 2:
            while check_file_exist('sessions.txt'):
                    check_account_number = input("Please provide your Account Number")
                    print("These are your Account details")
                    userAcctDetails = fetch_account_details(check_account_number)
                    print(f"1. Your account name is {userAcctDetails[0]} \n2.Your opening balance is {userAcctDetails[1]} \n3. Your account email is {userAcctDetails[2]} \n4. Your account type is {userAcctDetails[3]}\n5. Your account number is {userAcctDetails[4]}")
            show_account_options()

        elif account_options == 3:
            print("------------Thank you, You are logged out---------------")
            # delete user sessions
            import os
            if os.path.exists("sessions.txt"):
                os.remove("sessions.txt")
        else:
            print("------------Please Try again---------------")
    except ValueError:
        print("******Please Enter a valid number******")

genesis()
