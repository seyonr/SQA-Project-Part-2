# Import 
from print_error import log_constraint_error
from read import read_old_bank_accounts
from write import write_new_current_accounts

class Delete:
    def __init__(self, account_num, is_admin):
        self.account_num = account_num
        self.is_admin = is_admin

    def delete(self):
        file_path = ""  # Will be set to the path of the file itself
        accounts = read_old_bank_accounts(file_path) # Stores the accounts from the txt file 
        
        if(self.is_admin): # Handles admin deleting 
            # i is the index and x is the account at each element of the dictionary. -> Enumerate prevents the for loop from being a tuple
            for i, x in enumerate(accounts):
                if(int(x['account_number']) == self.account_num):
                    accounts.pop(i)
                write_new_current_accounts(accounts, file_path)
                return
        else: # Handles standrd resistrction
            log_constraint_error("Unprivileged User Error", "Standard user does not have admin privileges")

