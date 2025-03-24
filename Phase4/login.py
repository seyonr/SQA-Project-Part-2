from print_error import log_constraint_error
from read import read_old_bank_accounts

class Login:
    def __init__(self, account_num, account_name, is_admin):
        self.account_num = account_num
        self.account_name = account_name
        self.is_admin = is_admin

    def login(self):
        file_path = ""  # Set to correct path file
        accounts = read_old_bank_accounts(file_path)  # Load all valid accounts

        if(self.is_admin):
            for x in (accounts):
                if(int(x['account_number']) == self.account_num):
                    return True
                
                else:
                    log_constraint_error("Login Violation Error", "Account number does not exist")
            
        else:
            for x in (accounts):
                if(int(x['account_number']) == self.account_num):
                    if(x['name'] == self.account_name):
                        return True
                
                else:
                    log_constraint_error("Login Violation Error", "Account number does not exist")