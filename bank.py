import mysql.connector as con
mycon=con.connect(host="localhost" , user="root" , passwd="1" , database="bank")
if mycon.is_connected():
    print("Successfully Connected to MYSQL database.")
else:
    print("An error occur. Please try again.")

cur=mycon.cursor()  #buffered=True)

def mainmenu():
    print("*"*100)
    print("Welcome to YD BANK .".center(100))
    print("1. Create new account.".center(100))
    print("2. Display details of account holder.".center(100))
    print("   a. Shorted by account number.".center(100))
    print("   b. Shorted by customer name.".center(100))
    print("   c. Shorted by customer balance.".center(100))
    print("3. Search record details as per account number .".center(100))
    print("4. Update the account.".center(100))
    print("5. Delete the account.".center(100))
    print("6. Transactions (Debit , Credit & Withdraw) from the account.".center(100))
    print("   a. Debit/Withdraw from yhe account.".center(100))
    print("   b. Credit into the account.".center(100))
    print("7. Exit".center(100))
    print("*"*100)



def sort():
    print(" "*32,end=' ')
    print("="*33)
    print("a. Shorted by account number.".center(100))
    print("b. Shorted by customer name.".center(100))
    print("c. Shorted by customer balance.".center(100))
    print("d. Exit from here.".center(100))
    print(" "*32,end=' ')
    print("="*33)



def transaction():
    print(" "*30,end=' ')
    print("="*37)
    print("a. Debit/Withdraw from the account.".center(100))
    print("b. Credit into the account.".center(100))
    print("c. Exit from here.".center(100))
    print(" "*30,end=' ')
    print("="*37)



def create():
    try:
        cur.execute("create table bank(ACCNO int,NAME varchar(50),GENDER varchar(20),MOBILE INTEGER,EMAIL varchar(50),ADDRESS VARCHAR(100),CITY varchar(50),COUNTRY varchar(50),BALANCE DECIMAL ) ")
        print("Table Created.")
        Insert()
    except:
        print("Table already exist.")
        Insert()



def Insert():
    while True:      # Loop for accept the details.
        Acc=input("Enter account no. : ")
        Name=input("Enter name : ")
        Gender=input("Enter gender : ")
        Mob=input("Enter mobile no. : ")
        Email=input("Enter email address : ")
        Address=input("Enter address : ")
        City=input("Enter city : ")
        State=input("Enter State : ")
        Country=input("Enter country : ")
        Balance=input("Enter balance : ")
        #Rec=[Acc,Name.upper(),Gender.upper(),Mob,Email.upper(),Address.upper(),City.upper(),State.upper(),Country.upper(),Balance]
        Cmd="insert into BANK VALUES({},'{}','{}',{},'{}','{}','{}','{}','{}',{})".format(Acc,Name,Gender,Mob,Email,Address,City,State,Country,Balance)
        cur.execute(Cmd,)
        mycon.commit()
        ch=input("Do you want enter more records(y/n): ")
        if ch=='y' or ch=='Y' :
            continue
        elif ch=='n' or ch=='N':
            break



def sortacc():          #Function to display the records as per accending order of account number.
    try:
        cmd="select*from bank order by ACCNO"
        cur.execute(cmd)
        S=cur.fetchall()
        F="%15s %15s %15s %15s %15s %20s %13s %13s %13s %13s"
        print(F % ("Acc", "Name", "Gender", "Mobile", "Email", "Complete Address", "City", "State", "Country", "Balance"))
        print("*"*160)
        for i in S:
            for j in i:
                print("%15s" % j ,end=' ')
            print()
        print("*"*160)
    except:
        print("Table does not exit .")



def sortname():         #Function to display the records as per accending order of name.
    try:
        cmd="select*from bank order by NAME"
        cur.execute(cmd)
        S=cur.fetchall()
        F="%15s %15s %15s %15s %15s %20s %13s %13s %13s %13s"
        print(F % ("Acc", "Name", "Gender", "Mobile", "Email", "Complete Address", "City", "State", "Country", "Balance"))
        print("*"*160)
        for i in S:
            for j in i:
                print("%15s" % j ,end=' ')
            print()
        print("*"*160)
    except:
        print("Table does not exit .")

    


def sortbal():          #Function to display the records as per accending order of balance.
    try:
        cmd="select*from bank order by balance"
        cur.execute(cmd)
        S=cur.fetchall()
        F="%15s %15s %15s %15s %15s %20s %13s %13s %13s %13s"
        print(F % ("Acc", "Name", "Gender", "Mobile", "Email", "Complete Address", "City", "State", "Country", "Balance"))
        print("*"*160)
        for i in S:
            for j in i:
                print("%15s" % j ,end=' ')
            print()
        print("*"*160)
    except:
        print("Table does not exit .")



def searchacc():          #Function to search the account from the file with respect to the account number.
    try:
        cmd="select*from bank"
        cur.execute(cmd)
        S=cur.fetchall()
        ch=int(input("enter the account number to be searched : "))
        for i in S:
            i=list(i)
            if i[0]==ch:
                F="%15s %15s %15s %15s %15s %20s %13s %13s %13s %13s"
                print(F % ("Acc", "Name", "Gender", "Mobile", "Email", "Complete Address", "City", "State", "Country", "Balance"))
                print("="*160)
                for j in i:
                    print("%15s"% j ,end=' ')
                print()
                print("="*160)
                break
        else:
            print("Account does not exit.")
    except:
        print("Table does not exit .")



def update():
    try:
        cmd="select*from bank"
        cur.execute(cmd)
        S=cur.fetchall()
        A=int(input("enter the account number whose details updste : "))
        for i in S:
            i=list(i)
            if i[0]==A:
                ch=input("Change Name(y/n): ")
                if ch=='y' or ch=='Y':
                    i[1]=input("Enter Name: ")
                    i[1]=i[1].upper()

                ch=input("Change Gender(y/n): ")
                if ch=='y' or ch=='Y':
                    i[2]=input("Enter Gender: ")
                    i[2]=i[2].upper()

                ch=input("Change Mobile(y/n): ")
                if ch=='y' or ch=='Y':
                    i[3]=int(input("Enter Mobile: "))

                ch=input("Change Email(y/n): ")
                if ch=='y' or ch=='Y':
                    i[4]=input("Enter Email: ")
                    i[4]=i[4].upper()

                ch=input("Change Address(y/n): ")
                if ch=='y' or ch=='Y':
                    i[5]=input("Enter Address: ")
                    i[5]=i[5].upper()

                ch=input("Change City(y/n): ")
                if ch=='y' or ch=='Y':
                    i[6]=input("Enter City: ")
                    i[6]=i[6].upper()

                ch=input("Change State(y/n): ")
                if ch=='y' or ch=='Y':
                    i[7]=input("Enter State: ")
                    i[7]=i[7].upper()
                
                ch=input("Change Country(y/n): ")
                if ch=='y' or ch=='Y':
                    i[8]=input("Enter Country: ")
                    i[8]=i[8].upper()
                    
                ch=input("Change Balance(y/n): ")
                if ch=='y' or ch=='Y':
                    i[9]=float(input("Enter Balance: "))
                cmd-"update bank set Name=%s,Gender=%s,Mobile=%s,Email=%s,Address=%s,City=%s,State=%s,Country=%s,Balance=%s"
                val=(i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[0])
                cur.execute(cmd,val)
                mycon.commit()
                print("Account Updates.")
    except:
        print("Account does not exit .")



def delete():
    try:
        cmd="select*from bank"
        cur.execute(cmd)
        S=cur.fetchall()
        print("="*50)
        A=int(input("Enter the account number to be deleted: "))
        print("="*50)
        print("Countinue.......")
        for i in S:
            i=list(i)
            a=i[0]
            if a==A:
                print("="*110)
                print("Details of deleted account.")
                print(i)
                cmd="delete from bank where accno=%s"
                val=(i[0],)
                cur.execute(cmd,val)
                mycon.commit()
                print("="*110)
                print("Account Deleted.")
                break
        else:
            print("Account does not exist.")
    except:
        print("Account does not exist.")



def debit():
    try:
        cmd="select*from  bank"
        cur.execute(cmd)
        S=cur.fetchall()
        print("Please note that the money can be debited if minimum balance is Rs. 1000 exists.")
        A=int(input("Enter the account no. from which money is to be debited: "))
        for i in S:
            i=list(i)
            if i[0]==A:
                amt=int(input("Enter the ammount to be debited: "))
                if i[9]-amt>=1000:
                    i[9]-=amt
                    cmd="update bank set balance=%s where accno=%s"
                    val=(i[9],i[0])
                    cur.execute(cmd,val)
                    mycon.commit()
                    print("Amount Debited.")
                    break
                else:
                    print("There must be minimum balance Rs. 1000 required.")
                    break
        else:
            print("Account does not exsit.")
    except:
        print("Table does not exist.")



def credit():
    try:
        cmd="select*from  bank"
        cur.execute(cmd)
        S=cur.fetchall()
        A=int(input("Enter the account no. from which money is to be credited: "))
        for i in S:
            i=list(i)
            if i[0]==A:
                amt=int(input("Enter the ammount to be credited: "))
                i[9]=i[9]+amt
                cmd="update bank set balance=%s where accno=%s"
                val=(i[9],i[0])
                cur.execute(cmd,val)
                mycon.commit()
                print("Amount credited.")
                break
        else:
            print("Account does not exsit.")
    except:
        print("Table does not exist.")



while True:
    mainmenu()
    ch=input("Enter your choice: ")
    if ch=='1':
        Insert()
    elif ch=='2':
        while True:
            sort()
            a=input("Enter your choice: ")
            if a in ['a','A']:
                sortacc()
            elif a in ['b','B']:
                sortname()
            elif a in['c','C']:
                sortbal()
            elif a in ['d','D']:
                print("Back to mainmenu.......")
                break
            else:
                print("Invalid choice.")
    elif ch=='3':
        searchacc()
    elif ch=='4':
        update()
    elif ch=='5':
        delete()
    elif ch=='6':
        while True:
            transaction()
            a=input("Enter your choice: ")
            if a in ['a','A']:
                debit()
            elif a in ['b','B']:
                credit()
            elif a in['c','C']:
                print("Back to mainmenu.......")
                break
            else:
                print("Invalid choice.")
    elif ch=='7':
        print("Thank You for using our Bank.")
        print("Exiting.......")
        break
    else:
        print("Wrong choice entered.")
