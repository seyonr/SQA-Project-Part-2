# Import 
from print_error import log_constraint_error
from read import read_old_bank_accounts
from write_master import write_master_bank_accounts

class Paybill:
    # Constructor 
    def __init__(self, amount, account_num, is_admin):
        self.amount = amount
        self.account_num = account_num
        self.is_admin = is_admin

    # Handles paybill 
    def paybill(self):
        file_path = "accounts.txt" # Will be set to the path of the file itself
        accounts = read_old_bank_accounts(file_path) # Stores the accounts from the txt file 
        
        if(self.is_admin): # Handles admin paybill
            for x in accounts:
                if(int(x['account_number']) == self.account_num):
                    if(self.amount > int(x["balance"])): # Handles insufficent balance paybill
                        log_constraint_error("Balance Violation Error", "Insufficent balance")
                    else:
                        x["balance"] -= self.amount
                        write_master_bank_accounts(accounts, file_path) # Writes to file
                else:
                    log_constraint_error("Account Violation Error", "Account does not exisit")

        else: # Handles standard user paybill
            for x in accounts:
                if(int(x['account_number']) == self.account_num):
                    if(self.amount > 2000): # Handles stanard paybill limit
                        log_constraint_error("Withdrawl Limit Violation", "Standard user cannot withdraw above $2000")
                    
                    elif(self.amount > int(x["balance"])): # Handles insufficent balance paybill
                        log_constraint_error("Balance Violation Error", "Insufficent balance")

                    else:
                        x["balance"] -= self.amount
                        write_master_bank_accounts(accounts, file_path) # Writes to file
                else:
                    log_constraint_error("Account Violation Error", "Account does not exisit")
        