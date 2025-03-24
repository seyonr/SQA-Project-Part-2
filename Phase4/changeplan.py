# Import 
from print_error import log_constraint_error
from read import read_old_bank_accounts
from write import write_new_current_accounts

class ChangePlan:
    # Constructor 
    def __init__(self, account_num, is_admin, current_plan):
        self.account_num = account_num
        self.is_admin = is_admin
        self.current_plan = current_plan

    def change_plan(self):
        file_path = ""  # Will be set to the path of the file itself
        accounts = read_old_bank_accounts(file_path)  # Stores the accounts from the txt file 

        if(self.is_admin): # Handles admin changeplan
            for x in (accounts):
                if(int(x['account_number']) == self.account_num):
                    if (self.current_plan == "NP"):
                        self.current_plan = "SP"
                    else:
                        self.current_plan = "NP"
                    
                    write_new_current_accounts(accounts, file_path) # Write to file
                    return
                
                else:
                    log_constraint_error("Account Violation Error", "Account does not exisit")
            
        else: # Handles standard resistrction
            log_constraint_error("Unprivileged User Error", "Standard user does not have admin privileges")