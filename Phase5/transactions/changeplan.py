# Import 
from print_error import log_constraint_error
from read import read_old_bank_accounts
from write_master import write_master_bank_accounts

class ChangePlan:
    # Constructor 
    def __init__(self, account_num, is_admin):
        self.account_num = account_num
        self.is_admin = is_admin

    def change_plan(self):
        file_path = "accounts.txt" # Will be set to the path of the file itself
        accounts = read_old_bank_accounts(file_path)  # Stores the accounts from the txt file 

        if(self.is_admin): # Handles admin changeplan
            for x in (accounts):
                if(int(x['account_number']) == self.account_num):
                    if (x['plan'] == "NP"):
                        x['plan'] = "SP"
                    else:
                        x['plan'] = "NP"
                    
                    write_master_bank_accounts(accounts, file_path) # Writes to file
                    return
                
                else:
                    log_constraint_error("Account Violation Error", "Account does not exisit")
            
        else: # Handles standard resistrction
            log_constraint_error("Unprivileged User Error", "Standard user does not have admin privileges")