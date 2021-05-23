import random
import re
import time
class Bank_name:
    
#     '''def __init__(self, account_number=None, account_user_name=None):
#         self.account_number = account_number
#         self.account_user_name = account_user_name  '''
        
    def view_details(self):
        print("enter your account number : ")
        number = input(" ")
        file = open("detail_file.txt","r")
        get_number=" "
        while(get_number):
            get_number = file.readline()
            word = list(get_number.split())
            if number in word:
                #print("NAME     ACCOUNT_NO.    ADDRESS    PHONENUMBER      BALANCE \n")
                print(get_number)

    def create_an_account(self,account_user_name,account_number,emailid):
        account_user_name = input("  NAME :  ")
        print(f"Hello {account_user_name} we heartly Welcome you ! ! ! ")
        file = open("detail_file.txt","a+")
        file.write("\n")
        file.write("\n")
        file.write("  TIME :  ")
        local_time = time.ctime()
        file.write(local_time)
        file.write("  NAME :  ")
        file.write(account_user_name)
        file.write("  ACCOUNT_NUMBER :  ")
        account_number = account_user_name[0].upper() + account_user_name[1].upper() + str(random.randrange(1000000,10000000)) 
        file.write(account_number)
        print(" \t\t\t\tYOUR ACCOUNT_NUMBER is  ::  ",account_number)
        file.write("  ADDRESS :  ")
        print("Please enter the further details ! ")
        print("enter the your address  : ")
        address = input("  ADDRESS :  ")
        file.write(address)
        file.write(" EMAIL_ID :  ")
        print("Enter your Email ID : ")
        emailid = input(" EMAIL_ID :  ")
        regexeml = '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,3})$'
        if emailid != "":
            if (re.match(regexeml, emailid)):
                file.write(emailid)
                file.write(" ")
            else:
                print(" in valid Email ID")
                file.write("\t\t\t")
        print("enter your mobile number : ")
        phone_number = input("  PHONE_NUMBER :  ")
        regexphone = '^(\+\d{1,2}\s)?\(?\d{3}\)?\d{3}\d{4}$'
        if phone_number !=" ":
            if re.match(regexphone,phone_number):
                file.write("  PHONE_NUMBER :  ")
                file.write(phone_number)
            else:
                print("invalid phone number !!")
                file.write("\t\t\t")
             

        file.close()
    
 

    def add_money(self, account_user_name, account_number, money_amount):
        print("Enter amount of money you want to add : ")
        money_amount =  input("  MONEY:  ")
        file = open("detail_file.txt","a+")
        print("\t\t Enter account number for varification  : ")
        check_a_number = input("  ->  ")
        get_number = " "
        while(get_number):
            get_number = file.readline()
            word = get_number.split()
            if check_a_number in word:
                print("account exist !!")
        file.write("  MONEY :  ")
        file.write(money_amount)
        file.write(" ")
        file.close()             
    
    
                        
# #file = open("detail_file.txt","a+")
# #file.write("\n")
# #file.write("NAME     ACCOUNT_NO.    ADDRESS    PHONENUMBER      BALANCE")
# #file.close()    
emailid = None
account_number = None
account_user_name = None
money_amount = None
branch = Bank_name()
print("WELCOME ! ")
print("1. Login ")
print("2. Create a new account ")
choice = int(input("enter your choice : "))
if choice == 1:
     branch.view_details()
else:
    print("   Do you want to create an account  : (press y to continue !! )  ")    
    create_choice = input(" -> ")
    if create_choice == "y":
       branch.create_an_account(account_number,account_user_name,emailid)
       print("DO YOU WANT TO ADD MONEY IN YOUR ACCOUNT : (press y for yes) : ")
       press = input("  ->  ")
       if press == "y":
        branch.add_money(account_user_name, account_number, money_amount)
       else:
        print(" You logout succesfully !!!")    




