"""accounts={'609349699236':{'name':'Alex',
                          'balance':1000,
                          'pin':1234},
          '609349699237':{'name':'Hales',
                          'balance':10000,
                          'pin':1235},
          '609349699238':{'name':'Jason',
                          'balance':5000,
                          'pin':1236},
          '609349699239':{'name':'Roy',
                          'balance':2000,
                          'pin':1237},
}
print("="*50)
print("                 WELCOME TO ATM             ")
print("="*50)
acc_no=input('Enter Your Account Number: ')
if acc_no in accounts:
    crct_pin=accounts[acc_no]['pin']
    next_attempt=True
    a=1
    while a<4 and next_attempt:
        pin=int(input("Enter Your Pin: "))
        remaining=3-a
        a+=1
        session=False
        if pin==crct_pin:
            print('Proceed...')
            next_attempt=False
            session=True
        else:
            if remaining==0:
                print("Account Locked.Please visit after 24 Hours")
            else:
                print(f"{remaining} attempts left.Please Try Again")
    transaction_history=[]
    while session:
        print("Please Choose Your Option")
        print("1.Deposit")
        print("2.Withdraw")
        print("3.Balance Enquiry")
        print("4.Mini Statement")
        print("5.Pin Change")
        print("6.Exit")
        ch=int(input("Please Enter Your Choice Number: "))
        if ch==1:
            Deposit=int(input("Enter Your Deposit Amount: "))
            accounts[acc_no]['balance']+=Deposit
            transaction_history.append(f"{Deposit} Deposited Successfully")
            print(f"{Deposit} Deposited Successfully")
            print(f" current balance is {accounts[acc_no]['balance']}")

        elif ch==2:
            withdraw=int(input("Enter Your Withdraw Amount: "))
            if accounts[acc_no]['balance']>=withdraw:
                print(f" {withdraw}  withdrawn successfully" )
                accounts[acc_no]['balance']-=withdraw
                transaction_history.append(f" {withdraw}  withdrawn successfully")
                print(f"Remaining balance is {accounts[acc_no]['balance']}")
            else:
                print("Insufficient Funds")
        elif ch==3:
            print("Balance Checked Successfully: ")
            print(f"Available Balance is {accounts[acc_no]['balance']}")
        elif ch==4:
            n=len(transaction_history)
            i=n-1
            count=0
            while i>=0 and count<3:
                print(transaction_history[i])
                i-=1
                count+=1
        elif ch==5:
            cur_pin=int(input("Enter your current pin: "))
            if cur_pin==accounts[acc_no]['pin']:
                new_pin=int(input('Please enter your new pin:'))
                confirm=int(input('Please confirm your new pin:'))
                if new_pin==confirm:
                    accounts[acc_no]['pin']=new_pin
                    print(f"Pin updated successfully")
                else:
                    print("Confirmation Failed")
            else:
                print("Invalid Pin")
        elif ch==6:
            print("Thank You .Visit Again...")
            break
        else:
            print("invalid Choice")

        
else:
    print("Invalid Account Number")"""




'''lst=[1,2,3,4,5]
n=len(lst) 
count=0
for i in range(n-1,0,-1):
    if count<3:
        print(lst[i])
    count+=1
'''
l=[1,2,3,5,4,3]
n=len(l)
largest=l[0]
sec=0
for i in range(1,n):
    if l[i]>largest:
        largest=l[i]
        l[i]=sec
for i in range(1,n):
    if l[i]>sec and sec!=largest:
        sec=l[i]
print(sec)


