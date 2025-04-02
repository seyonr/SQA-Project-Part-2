# Import 
from print_error import log_constraint_error
from read import read_old_bank_accounts
from update import update

class Deposit:
    # Constructor
    def __init__(self, amount, account_num, is_admin):
        self.amount = amount
        self.account_num = account_num
        self.is_admin = is_admin

    def deposit(self):
        file_path = "accounts.txt" # Will be set to the path of the file itself
        accounts = read_old_bank_accounts(file_path)   # Stores the accounts from the txt file 

        if(self.is_admin): # Handles admin deposit
            for x in accounts:
                if(int(x['account_number']) == self.account_num):
                    if(x['plan'] == "NP"):
                        x['total_transactions'] += 1
                        x["balance"] += self.amount - 0.1  # Deducting 10 cents for "non-student" plan
                    elif(x['plan'] == "SP"):
                        x['total_transactions'] += 1
                        x["balance"] += self.amount - 0.05 # Deducting 5 cents for "student" account.
                    
                    update(accounts, file_path)
                    return
                else:
                    log_constraint_error("Account Violation Error", "Account does not exisit")
        else: # Handles standard user deposit
            for x in accounts:
                if(int(x['account_number']) == self.account_num):
                    if(x['plan'] == "NP"):
                        x['total_transactions'] += 1
                        x["balance"] += self.amount - 0.1  # Deducting 10 cents for "non-student" plan
                    elif(x['plan'] == "SP"):
                        x['total_transactions'] += 1
                        x["balance"] += self.amount - 0.05 # Deducting 5 cents for "student" account.
                    
                    update(accounts, file_path)
                    return
                else:
                    log_constraint_error("Account Violation Error", "Account does not exisit")
