def fetch_user_details():
    with open('staff.txt') as f:
        read_data = f.readlines()
        f.close()
        return read_data

def remove_session(filename):
  import os
  if os.path.exists(filename):
    os.remove(filename)

def store_user_sessions(username,password):
    with open('session.txt','w') as f:
        f.write('{}\n'.format(username))
        f.write('{}\n'.format(password))

def check_file_exist(filename):
  import os
  if os.path.exists(filename):
    return True

def get_account_no(n):
  from random import randint
  start = 10**(n-1)
  end = (10**n)-1
  return randint(start,end)

def store_account_details(acct_list):
  with open('customer.txt', 'w') as file_handler:
    for item in acct_list:
      file_handler.write("{}\n".format(item))

def fetch_account_details(acctno):
  with open('customer.txt', 'r') as f:
      read_data = f.readlines()
      f.close()
      if acctno == read_data[4].strip('\n'):
        return read_data

def show_account_options(session):
    try:
        account_options = int(input("Please select your preferred option option 1. Create new bank account \n2. Check Account Details \n3. Logout  "))
        if account_options == 1:
            # get user account details for creating account
            accountName = input("Please input the Account name")
            openingBalance = input("Please input the Opening balance")
            accountType = input("Please input the Account Type")
            accountEmail = input("Please input the Account Email")
            accountNumber = get_account_no(10)
            accountDetails = [accountName, openingBalance, accountType, accountEmail, accountNumber]
            # Store details in customer file
            store_account_details(accountDetails)
            print(f'Your account has been created with account number {accountNumber}')
            show_account_options(session)

            # print("Account created")
        elif account_options == 2:
            while check_file_exist('sessions.txt'):
                enteredaccountNumber = input("Please provide your Account Number")
                print("These are your Account details")
                userAcctDetails = fetch_account_details(enteredaccountNumber)

                print(f"1. Your account name is {userAcctDetails[0]} \n2.Your opening balance is {userAcctDetails[1]} \n3. Your account email is {userAcctDetails[2]} \n4. Your account type is {userAcctDetails[3]}\n5. Your account number is {userAcctDetails[4]}")

        elif account_options == 3:
            print("------------Please You are logged out---------------")
            # delete user sessions
            remove_session('session.txt')
        else:
            print("------------Please Try again---------------")
    except ValueError:
        print("******Please Enter a valid number******")

def login_and_close():
    try:
        while True:
            options = int(input("please enter 1 to login \nor \n2 to close:"))
            if options == 1:
                print("--------------WELCOME TO SNBANK---------------")
                username = input("please enter your preferred username: ")
                password = input("please enter your password:")
                staffdetails = fetch_user_details()
                username_input=[staffdetails[0].strip('\n'),staffdetails[4].strip('\n')]
                password_input=[staffdetails[1].strip('\n'),staffdetails[5].strip('\n')]
                if username in username_input and password in password_input:
                    print("----------You are logged in--------------")
                    # store user data in file sessions
                    newSession = store_user_sessions(username, password)
                    # Display account opitions
                    show_account_options(newSession)
                else:
                    print("------------Please Try again---------------\nYour credentials do not match any record")
            elif options == 2:
                print("Closing App ...")
                break
            else:
                print("------------Please Try again---------------")
    except ValueError:
        print("******Please Enter a valid number******")

login_and_close()