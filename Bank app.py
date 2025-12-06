print("=" * 40)
print("        WELCOME TO ARI'S BANK        ")
print("=" * 40)

Name = input("Enter your Name: ")
print(Name)


attempts = 3

while attempts > 0:
    password = input("Enter your 4 digit Password: ")
    
    if len (password) == 4 and password.isdigit():
     print("password accepted...")
     break
    else:
        attempts = attempts -1
        print(" Wrong Password", attempts, "left")
if attempts == 0:
    print("Account locked.!!")
    exit()
transaction = []

balance = 0.0
print("Your opening Balance is:", balance)

while True:
    print("=" * 40)
    print("\nPlease choose an option:")
    print("1. Deposit")
    print("2. Withdrawal")
    print("3. Transaction History")
    print("4. Exit")
    print("=" * 40)

    choice =input("Enter your choice (1/2/3/4): ")
    
    if choice == "1":
        amount =float(input("Enter you deposit amount: "))
        balance =  balance + amount
        print("£", amount, "has been added!!!")
        print("Your New balance is :", balance)
        transaction.append(f"Deposited £{amount}")


    elif choice == "2":
        amount = float(input("Enter you withdrawl amount:"))
        if amount>balance:
            print("Insufficient Balance")
        else:
            balance = balance - amount
            print("£", amount, "has been withdrawn")
            print ("Your new balance is :", balance)
            transaction.append(f"Withdrawl £ {amount}")
            
    elif choice == "3":
        
        print ("Transaction History ")
        if len (transaction) == 0:
            print("No Transaction yet ")
        else:
            for t in transaction:    #t is a variable to check the list in transation. 
                print(t)

    elif choice == "4":
        print ("Thank you")
        break
    else:
        print("Invalid option Please choose deposit, withdrawl or exit")





    
    





