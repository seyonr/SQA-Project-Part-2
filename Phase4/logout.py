from read import read_old_bank_accounts
from write import write_new_current_accounts
from write_master import write_master_bank_accounts

class Logout:
    def __init__(self, new_master_path, current_account_path):
        self.new_master_path = new_master_path
        self.current_account_path = current_account_path


    def logout(self):
        accounts = read_old_bank_accounts("accounts.txt") 

        write_new_current_accounts(accounts, self.current_account_path)
        write_master_bank_accounts(accounts, self.new_master_path)
    
        