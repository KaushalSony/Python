import mysql.connector as sq
def connect():
    db=sq.connect(host='localhost',user='root',passwd="abcd1234",database='billing')
    if db.is_connected==False:
        print("not connected")
    return db
def bill():
    print("-----------------------WELCOME TO BILLING SOFTWARE-------------------------")
    print("1.STOCK MANAGEMENT")
    print("2.COSTOMER MANAGEMENT/BILL MAKING")
    ch=int(input("enter your choice(1-2):-"))
    if ch==1:
        print("\n------------------WELCOME TO STOCK MANAGEMENT------------------\n")
        print("a.VIEWING STOCK")
        print("b.INSERT NEW ITEM IN THE STOCK")
        print("c.UPDATE STOCK")
        def displayst():
            con=connect()
            cur=con.cursor()
            cur.execute("select * from Stock")
            for i in cur.fetchall():
                S_ID=i[0]
                Descripion=i[1]
                Brand=i[2]
                Qty=i[3]
                Price=i[4]
                print("(S_ID=%d,Descripion=%s,Brand=%s,Qty=%s,Price=%s)"%(S_ID,Descripion,Brand,Qty,Price))
                
        c=input("enter your choice(a-c):-")
        if c=='a':
            displayst()
        elif c=='b':
            def insert():
                con=connect()
                cur=con.cursor()
                S_ID=int(input("ENTER S_ID OF THE ITEM. :-"))
                Descripion=input("ENTER NAME OF THE ITEM. :-")
                Brand=input("ENTER BRAND OF THE ITEM. :-")
                Qty=int(input("ENTER QUANTITY OF ITEM:-"))
                Price=int(input("ENTER PRICE OF THE ITEM. :-"))
                cur.execute("insert into stock values ('%d','%s','%s','%d','%d')"%(S_ID,Descripion,Brand,Qty,Price))
                con.commit()
            insert()
            displayst()
        elif c=='c':
            def update():
                con=connect()
                cur=con.cursor()
                Qty=int(input("ENTER QUANTITY TO BE ADDED:-"))
                S_ID=int(input("ENTER S_ID OF THE ITEM. :-"))
                cur.execute("update Stock set Qty=Qty+%d where S_ID=%d"%(Qty,S_ID))
                con.commit()
            update()
            displayst()
    elif ch==2:
        print("\n------------------WELCOME TO CUSTOMER MANAGEMENT/BILL MAKING------------------\n")
        print("a.VIEWING CUSTOMER LIST")
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
                s={}
                c={}
                c1={}
                s1={}
                con=connect()
                cur=con.cursor()
                cur.execute("select * from Stock")
                for i in cur.fetchall():
                    S_ID=i[0]
                    Description=i[1]
                    Brand=i[2]
                    Qty=i[3]
                    Price=i[4]
                    s[Description]=Price
                    s1[Description]=Brand
                cur.execute("select * from customer")
                for i in cur.fetchall():
                    Invoice_No=i[1]
                    Name=i[2]
                    Address=i[3]
                    Phone=i[4]
                    Item_Purchased=i[5]
                    Brand=i[6]
                    Date_of_Purchase=i[7]
                    c[Name]=Address
                    c1[Name]=Phone
            
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
                    Price=s[Description]
                    B=s1[Description]
                    qty=int(input('Enter Quantity Required :'))
                    val = Price * qty
                    a = a + val
                    dict[Description]=B,qty,Price,val
                    CGST= a*5/100
                    SGST=CGST
                    net =a+CGST+SGST
                    cur.execute("update Stock set Qty=Qty-%d where Description='%s'"%(qty,Description))
                    cur.execute("insert into customer(Invoice_No,Name,Address,Phone,Item_Purchased,Brand,Date_of_Purchase) values('%d','%s','%s','%d','%s','%s','%s')"%(I,N,A,P,Description,B,dtm))
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
                b={}
                b1={}
                con=connect()
                cur=con.cursor()
                cur.execute("select * from Stock")
                for i in cur.fetchall():
                    S_ID=i[0]
                    Description=i[1]
                    DescriptionL=i[1]
                    Brand=i[2]
                    Qty=i[3]
                    Price=i[4]
                    b[Description]=Brand
                    b1[DescriptionL]=Brand
                Invoice_No=int(input("Enter Invoice No:-"))
                Description=input("Enter Name of New Item Purchased:-")
                Brand=b[Description]
                DescriptionL=input("Enter Name of Old Item Purchased:-")
                Brands=b[DescriptionL]
                cur.execute("update customer set Item_Purchased='%s',Brand='%s' where Invoice_No=%d and Item_Purchased='%s' and Brand='%s'"%(Description,Brand,Invoice_No,DescriptionL,Brands))
                con.commit()
            update()
            displaycu()
            
bill()
