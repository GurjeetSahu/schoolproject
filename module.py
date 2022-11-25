def verification(accno, password, cursor, typ):
    if typ == 1:
        cursor.execute(
            "SELECT accountNo,password FROM customer_info WHERE accountNo = {acc};".format(acc=accno))
    elif typ == 2:
        cursor.execute(
            "SELECT emp_ID,password FROM emp_details WHERE emp_ID = {acc};".format(acc=accno))
    else:
        print("Please Choose From 1 and 2")

    data = cursor.fetchone()
    if data[1] == password:
        print("Verification Successfull!")
        return True
    else:
        return False


def openAccount(empno, cursor, con):
    name = input("Enter Name: ")
    typ = input("Enter account type: ")
    initBal = 5000
    pwd = input("Enter Password: ")
    contact = int(input("Enter contact: "))

    cursor.execute(
        "INSERT INTO customer_info (name, balance, account_type, password,contact_no) VALUES ('{name}','{initBal}','{typ}','{pwd}','{no}')".format(name=name, typ=typ, initBal=initBal, pwd=pwd, no=contact))
    cursor.execute("SELECT MAX(accountNo) FROM customer_info")
    lastNo = cursor.fetchone()[0]
    cursor.execute(
        "INSERT INTO transactions (type,accontNo,datetime,empNo) VALUES('openacc','{accno}',NOW(),'{empno}')".format(accno=lastNo, empno=empno))
    con.commit()
    cursor.execute("SELECT MAX(accountNo) FROM customer_info")
    no = cursor.fetchone()[0]
    print("Success! Your Account Number is: {no}".format(no=no))


def remAccount():
    pass


def withdraw(accno, cursor, con):
    amount = float(input("Enter withdrawal amount: "))
    cursor.execute("UPDATE customer_info SET balance = balance-{am} WHERE accountNo ={acno};".format(
        am=amount, acno=accno))
    cursor.execute("INSERT INTO transactions (type,accontNo,datetime,transaction_amount) VALUES('withdraw','{accountNo}',Now(),'{amount}')".format(
        accountNo=accno, amount=-amount))
    con.commit()
    cursor.execute(
        "SELECT balance from customer_info where accountNo={acc}".format(acc=accno))
    curBal = (cursor.fetchone())[0]
    print("Success! \nCurrent Balance: {bal}".format(bal=curBal))


def deposit(accno, cursor, con):

    # Adds Balance To Account
    amount = float(input("Put Amount in Cash Box: "))
    cursor.execute("UPDATE customer_info SET balance = balance+{am} WHERE accountNo ={acno};".format(
        am=amount, acno=accno))

    cursor.execute("INSERT INTO transactions (type,accontNo,datetime,transaction_amount) VALUES('deposit','{accountNo}',Now(),'{amount}')".format(  # updates record
        accountNo=accno, amount=amount))
    con.commit()

    cursor.execute(  # prints final balance
        "SELECT balance from customer_info where accountNo={acc}".format(acc=accno))
    curBal = cursor.fetchone()[0]
    print("Success! \nCurrent Balance: {bal}".format(bal=curBal))


def inquiry(accno, cursor):
    cursor.execute(
        "SELECT name,balance,account_type from customer_info where accountNo={acc};".format(acc=accno))
    data = cursor.fetchone()
    print("Account Holder's Name: {name} \nBalance: {bal} \nType: {typ}".format(
        name=data[0], bal=data[1], typ=data[2]))


def transHistory(accno, cursor):
    cursor.execute(
        "SELECT datetime,type,transaction_amount from transactions where accontNo={acc};".format(acc=accno))
    data = cursor.fetchall()
    for rec in data:
        print((rec[0]), rec[1], rec[2])
