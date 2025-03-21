from print_error import log_constraint_error
from read import read_old_bank_accounts
from write import write_new_current_accounts

class Deposit:
    def __init__(self, amount, account_num, is_admin):
        self.amount = amount
        self.account_num = account_num
        self.is_admin = is_admin

    def deposit(self):
        file_path = ""  # Set to correct path file
        accounts = read_old_bank_accounts(file_path)  # Will hold all valid accounts

        if(self.is_admin): # Admin code handle
            for x in accounts:
                if(int(x['account_number']) == self.account_num):
                    if(x['plan'] == "NP"):
                        x["balance"] += self.amount - 0.1  # Deducting 10 cents for "non-student" plan
                    elif(x['plan'] == "SP"):
                        x["balance"] += self.amount - 0.05 # Deducting 5 cents for "student" account.
                    write_new_current_accounts(accounts, file_path)
                else:
                    log_constraint_error("Account Violation Error", "Account does not exisit")
        else:
            for x in accounts:
                if(int(x['account_number']) == self.account_num):
                    if(x['plan'] == "NP"):
                        x["balance"] += self.amount - 0.1  # Deducting 10 cents for "non-student" plan
                    elif(x['plan'] == "SP"):
                        x["balance"] += self.amount - 0.05 # Deducting 5 cents for "student" account.
                    write_new_current_accounts(accounts, file_path)
                else:
                    log_constraint_error("Account Violation Error", "Account does not exisit")
