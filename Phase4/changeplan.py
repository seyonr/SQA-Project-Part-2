from print_error import log_constraint_error
from read import read_old_bank_accounts
from write import write_new_current_accounts

class ChangePlan:
    def __init__(self, account_num, is_admin):
        self.account_num = account_num
        self.is_admin = is_admin

    def change_plan(self):
        file_path = ""  # Set to correct path file
        accounts = read_old_bank_accounts(file_path)  # Load all valid accounts

        if(self.is_admin):
            for x in (accounts):
                if(int(x['account_number']) == self.account_num):
                    if ((x['plan']) == "NP"):
                        x['plan'] = "SP"
                    else:
                        x['plan']="NP"
                    
                    write_new_current_accounts(accounts, file_path)
                    return
                
                else:
                    log_constraint_error("Account Violation Error", "Account does not exisit")
            
        else:
            log_constraint_error("Unprivileged User Error", "Standard user does not have admin privileges")