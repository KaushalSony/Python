import mysql.connector as sq
import pandas as pd
import matplotlib.pyplot as plt

def connect():
    db=sq.connect(host='localhost',user='root',passwd="abcd1234",database='billing')
    if db.is_connected==False:
        print("not connected")
    return db
def bill():
    print("-----------------------WELCOME TO BILLING SOFTWARE-------------------------")
    print("1.STOCK MANAGEMENT")
    print("2.COSTOMER MANAGEMENT/BILL MAKING")
    print("3.Graphical Representation of Overall Sale")
    ch=int(input("enter your choice(1-3):-"))
    if ch==1:
        print("\n------------------WELCOME TO STOCK MANAGEMENT------------------\n")
        print("a.VIEWING STOCK")
        print("b.INSERT NEW ITEM IN THE STOCK")
        def displayst():
            df=pd.read_csv("C:\\Users\\KM SONI\\Desktop\\Billing.csv")
            print(df)                
        c=input("enter your choice(a-b):-")
        if c=='a':
            displayst()
        elif c=='b':
            def insert():
                con=connect()
                cur=con.cursor()
                df=pd.read_csv("C:\\Users\\KM SONI\\Desktop\\Billing.csv")
                n=int(input('Enter No. of Items to be added'))
                for i in range(0,n):
                    S_No=int(input("ENTER S_ID OF THE ITEM. :-"))
                    Item_Name=input("ENTER NAME OF THE ITEM. :-")
                    Brand=input("ENTER BRAND OF THE ITEM. :-")
                    Price=int(input("ENTER PRICE OF THE ITEM. :-"))
                    cur.execute("insert into sales(Sl_No,Item_Purchased) values ('%d','%s')"%(S_No,Item_Name))
                    con.commit()
                    d={'S_ID':S_No, 'Item_Name':Item_Name,'Brand':Brand, 'Price':Price}
                    df1=pd.DataFrame(d,index=range(n))
                    df=df.append(df1)
                df2=df.to_csv("C:\\Users\\KM SONI\\Desktop\\Billing.csv",index=False)
            insert()
            displayst()
    elif ch==2:
        print("\n------------------WELCOME TO CUSTOMER MANAGEMENT/BILL MAKING------------------\n")
        print("a.VIEWING CUSTOMER Details")
        print("b.INSERT CUSTOMER RECORDS ALONG WITH MAKING BILL")
        print("c.UPDATE CUSTOMER RECORDS(CHANGES IN ITEM PURCHASED NAME AND BRAND)")
        
        def displaycu():
            con=connect()
            cur=con.cursor()
            cur.execute("select * from customer")
            for i in cur.fetchall():
                S_No=i[0]
                Invoice_No=i[1]
                Name=i[2]
                Address=i[3]
                Phone=i[4]
                Item_Purchased=i[5]
                Brand=i[6]
                Date_of_Purchase=i[7]
                print("(S_No=%d,Invoice_No=%d,Name=%s,Address=%s,Phone=%d,Item_Purchased=%s,Brand=%s,Date_of_Purchase=%s)"%(S_No,Invoice_No,Name,Address,Phone,Item_Purchased,Brand,Date_of_Purchase))
                
        c=input("enter your choice(a-c):-")
        if c=='a':
            displaycu()
        elif c=='b':
            def insert():
                c={}
                c1={}
                con=connect()
                cur=con.cursor()
                cur.execute("select * from customer")
                for i in cur.fetchall():
                    Invoice_No=i[1]
                    Name=i[2]
                    Address=i[3]
                    Phone=i[4]
                    Item_Purchased=i[5]
                    Brand=i[6]
                    Date_of_Purchase=i[7]
            
                import datetime
                now=datetime.date.today()
                dtm=str(now)
                n=int(input('Enter Total Number of Items:'))
                a =0
                dict={}
                N=input("Enter Customer's Name: ")
                A=input("Enter Customer's Address: ")
                P=int(input("Enter Customer's Phone Number: "))
                I=int(input("Enter Involce Number: "))
                for i in range(1,n+1,1):
                    con=connect()
                    cur=con.cursor()
                    Description=input('Enter Name of Item :')
                    Price=int(input('Enter Price of the Item :'))
                    B=input('Enter Brand of Item :')
                    qty=int(input('Enter Quantity Required :'))
                    val = Price * qty
                    a = a + val
                    dict[Description]=B,qty,Price,val
                    CGST= a*5/100
                    SGST=CGST
                    net =a+CGST+SGST
                    cur.execute("update sales set Qty=Qty+%d where Item_Purchased='%s'"%(qty,Description))
                    con.commit()
                    cur.execute("insert into customer(C_ID,Name,Address,Phone,Item_Purchased,Brand,Date_of_Purchase) values('%d','%s','%s','%d','%s','%s','%s')"%(I,N,A,P,Description,B,dtm))
                    con.commit()
                print('-'*85)
                print('\t\t\t\t  INVOICE')
                print('\t\t\t\tABC COMPUTERS')
                print('-'*85)
                print('\t\t\t\t\t\t\t\t     date:',dtm)
                print('\t\t\t\t\t\t\t\t     Invoice No.:',I)
                print('-'*85)
                print('Bill To:')
                print('Name:',N)
                print('Address:',A)
                print('Phone No.:',P)
                print('-'*85)
                print('ITEM\t\t\t\tBrand\t\tQuantity\tUnit Price\tValue')
                print('-'*85)

                for k,v in dict.items():
                    print('{0:<25s}'.format(k),end=' ')
                    print('{0:>18s}'.format(v[0]),end=' ')
                    print('{0:>11d}'.format(v[1]),end=' ')
                    print('{0:>17.2f}'.format(v[2]),end=' ')
                    print('{0:>10.2f}'.format(v[3]))
                print('-'*85)
                print('CGST:{0:>80.2f}'.format(CGST))
                print('SGST:{0:>80.2f}'.format(SGST))
                print('-'*85)
                print('Amount Payable:{0:>70.2f}'.format(net))
                print('-'*85)


            insert()
        elif c=='c':
            def update():
                con=connect()
                cur=con.cursor()
                Invoice_No=int(input("Enter Invoice No:-"))
                Item_Purchase=input("Enter Name of New Item Purchased:-")
                Brand=input("Enter Brand of New ITEM:-")
                Item_Purchased=input("Enter Name of Old Item Purchased:-")
                Brands=input("Enter Brand of Old ITEM:-")
                cur.execute("update customer set Item_Purchased='%s',Brand='%s' where C_ID=%d and Item_Purchased='%s' and Brand='%s'"%(Item_Purchase,Brand,Invoice_No,Item_Purchased,Brands))
                con.commit()
            update()
            displaycu()
    elif ch==3:
        print("\n------------------WELCOME TO GRAPHICAL REPRESENTATION OF SALE------------------\n")
        def show():
            con=connect()
            d=pd.read_sql('select * from sales',con)
            d.plot(x='Item_Purchased',y='Qty',kind='bar')
            plt.title('Overall sale')
            plt.show()
        show()
        

            
bill()
