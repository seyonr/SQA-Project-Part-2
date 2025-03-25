# Import 
from print_error import log_constraint_error
from read import read_old_bank_accounts
from write_master import write_master_bank_accounts

class Deposit:
    # Constructor
    def __init__(self, amount, account_num, is_admin, current_plan):
        self.amount = amount
        self.account_num = account_num
        self.is_admin = is_admin
        self.current_plan = current_plan

    def deposit(self):
        file_path = "accounts.txt" # Will be set to the path of the file itself
        accounts = read_old_bank_accounts(file_path)   # Stores the accounts from the txt file 

        if(self.is_admin): # Handles admin deposit
            for x in accounts:
                if(int(x['account_number']) == self.account_num):
                    if(self.current_plan == "NP"):
                        x["balance"] += self.amount - 0.1  # Deducting 10 cents for "non-student" plan
                    elif(self.current_plan == "SP"):
                        x["balance"] += self.amount - 0.05 # Deducting 5 cents for "student" account.
                    write_master_bank_accounts(accounts, file_path) # Writes to file
                else:
                    log_constraint_error("Account Violation Error", "Account does not exisit")
        else: # Handles standard user deposit
            for x in accounts:
                if(int(x['account_number']) == self.account_num):
                    if(x['plan'] == "NP"):
                        x["balance"] += self.amount - 0.1  # Deducting 10 cents for "non-student" plan
                    elif(x['plan'] == "SP"):
                        x["balance"] += self.amount - 0.05 # Deducting 5 cents for "student" account.
                    write_master_bank_accounts(accounts, file_path) # Writes to file
                else:
                    log_constraint_error("Account Violation Error", "Account does not exisit")
