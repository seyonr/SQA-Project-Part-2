# Import 
from print_error import log_constraint_error
from read import read_old_bank_accounts
from update import update

class Disable:
    # Constuctor 
    def __init__(self, account_num, is_admin):
        self.account_num = account_num
        self.is_admin = is_admin

    def disable(self):
        file_path = "accounts.txt" # Will be set to the path of the file itself
        accounts = read_old_bank_accounts(file_path) # Stores the accounts from the txt file 
        
        if(self.is_admin): # Handles admin disable
            for x in (accounts):
                if(int(x['account_number']) == self.account_num):
                    if ((x['status']) == "A"):
                        x['status'] = "D"
                    else:
                        x['status']="A"
                    
                    update(accounts, file_path)
                    return
                
                else: # Handles standard resistrction 
                    log_constraint_error("Account Violation Error", "Account does not exisit")
                
        else: # Handles standard user disable 
           log_constraint_error("Unprivileged User Error", "Standard user does not have admin privileges")

