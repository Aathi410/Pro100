class Atm:
    def __init__(self,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin

    def check_balance(self):
        print("Your Balance Is 10000")

    def withdrawl(self,amount):
        new_amount = 10000 - amount
        print("You Have Withdrawn "+str(amount) +". Your remaining balance is "+ str(new_amount))

def main():
    Card_number = input("Enter Your Card Number:- ")
    pin_number  = input("enter Your Pin Number:- ")
    new_user =  Atm(Card_number ,pin_number)
    print("Choose Activity ")
    print("1.Balance Enquriy   2.withdrawl")
    activity = int(input("Enter Your Activity Number :- "))

    if (activity == 1):
        new_user.check_balance()
    elif (activity == 2):
        amount = int(input("Enter Amount:- "))
        new_user.withdrawl(amount)
    else:
        print("Enter The Valid Number")

if __name__ == "__main__":
    main()