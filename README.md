# snbank
a banking system management with CRUD properties 

On run, the program presents the following options:

1 Staff Login

2 Close App

If the user selects Login, the user would be asked for their username and password, the program would check the pre-defined staff in a file called staff.txt and verify that the username and password are correct. If incorrect, user would see an error message and be told to try again. 

After user login is successful, a new file would be created to store the user session.

After login, staff would be presented with the following options: 

1 Create new bank account

2 Check Account Details

3 Logout

If staff selects Create bank account, 

staff would be made to supply the following

Account name

Opening Balance

Account Type

Account email

The details above would be saved in the customer.txt file, before saving,  a 10 digits account number is generated for the customer.

After staff completes creating the account, they would see the account number, and are presented with the options in (4) above.

If Staff selects check account details from (4) above, the program would request for account number

The program would fetch the details of the account from the customer.txt file and display it to the staff, then present back the options in (4) above.

If staff selects logout in (4) above, delete the user session file and return the user back to the staff login page.

 

And finally, if staff selects Close App, the program should terminate.
