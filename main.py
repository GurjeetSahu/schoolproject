import module
import mysql.connector as connector

con = connector.connect(host="localhost", user="root",
                        passwd="root", database="bankmanagement")
cursor = con.cursor()

print("Welcome to State Bank of India.")
typ = int(input("1. ATM Services. \n2. Staff Login. \nPlease Choose: "))
accno = int(input("Enter Account/Employee Number: "))
password = input("Enter password: ")

if typ == 1 and module.verification(accno, password, cursor, typ) == True:
    act = int(input(
        "1.Deposit Money \n2.Withdraw Money \n3.Balance Enquiry \n4.View previous Transactions \nPlease choose action: "))
    if act == 1:
        module.deposit(accno, cursor, con)
    elif act == 2:
        module.withdraw(accno, cursor, con)
    elif act == 3:
        module.inquiry(accno, cursor)
    elif act == 4:
        module.transHistory(accno, cursor)

elif typ == 2 and module.verification(accno, password, cursor, typ) == True:
    act = int(input("1.Add Account. \n2.Remove Account"))
    if act == 1:
        module.openAccount(accno, cursor, con)
else:
    print("Cannot Verify! Pleas Try Again.")
