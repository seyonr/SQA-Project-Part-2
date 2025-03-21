from print_error import log_constraint_error
from read import read_old_bank_accounts
from write import write_new_current_accounts

class Disable:

    def __init__(self, account_num, is_admin):
        self.account_num = account_num
        self.is_admin = is_admin

    def disable(self):
        file_path = ""  # Set to correct path file
        accounts = read_old_bank_accounts(file_path) 
        
        if(self.is_admin): # Admin code handle
            for x in (accounts):
                if(int(x['account_number']) == self.account_num):
                    if ((x['status']) == "A"):
                        x['status'] = "D"
                    else:
                        x['status']="A"
                    
                    write_new_current_accounts(accounts, file_path)
                    return
                
                else:
                    log_constraint_error("Account Violation Error", "Account does not exisit")
                
        else:
           log_constraint_error("Unprivileged User Error", "Standard user does not have admin privileges")

