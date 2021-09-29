

class ATM:
    def __init__(self,card_number,account_number,branch_name,withdrawal_amount):
        self.card_number=card_number
        self.account_number=account_number
        self.branch_name=branch_name
        self.widthdrawal_amount=withdrawal_amount

print("Hey!Welcome to Kotak Mahindra Bank! I am Nina , your assistant and I will help you withdraw money from your account!")
accountNumber=input("Enter the account number, please!")
print("OK!Good,now...")
cardNumber=input("Enter the card number")
branchName=input("Enter full branch name with city,please!")
widthdrawalAmount = input("Enter amount to be widthdrawn.")
print("  ")
print("Processing...")
transaction_1=ATM(cardNumber,accountNumber,branchName,widthdrawalAmount)
print("  ")
print("Transcation successful!")
print("---details----")
print("account number:" +accountNumber)
print("kotak branch:"+branchName)
print("widthdrawal amount:"+widthdrawalAmount)
print("---------------")
print("  ")
print("Thank you for using Kotak services!See you next time!")

