# Import 
from print_error import log_constraint_error
from read import read_old_bank_accounts
from write_master import write_master_bank_accounts

class Create:
    # Constructor 
    def __init__(self, amount, account_num, account_name, status, is_admin, plan):
        self.amount = amount
        self.account_num = account_num
        self.account_name = account_name
        self.status = status
        self.is_admin = is_admin
        self.plan = plan

    def create(self):
        file_path = "accounts.txt" # Will be set to the path of the file itself
        accounts = read_old_bank_accounts(file_path)  # Stores the accounts from the txt file 

        # Adding new account to file
        if self.is_admin:
            accounts.append({
                'account_number' : self.account_num,
                'name': self.account_name,
                'status': self.status,
                'balance': self.amount,
                'total_transactions': 0,
                'plan': self.plan
            })
            write_master_bank_accounts(accounts, file_path) # Writes to file
        else: # Handles standrd resistrction
            log_constraint_error("Unprivileged User Error", "Standard user does not have admin privileges")