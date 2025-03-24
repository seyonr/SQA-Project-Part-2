# Imports
from print_error import log_constraint_error
from read import read_old_bank_accounts
from write import write_new_current_accounts

class Transfer:
    # Constructor 
    def __init__(self, amount, account_num_from, account_num_to, is_admin):
        self.amount = amount
        self.account_num_from = account_num_from
        self.account_num_to = account_num_to
        self.is_admin = is_admin

    # Function which handles transfer
    def transfer(self):
        file_path = "" # Will be set to the path of the file itself
        accounts = read_old_bank_accounts(file_path) # Stores the accounts from the txt file 
        
        if(self.is_admin): # Handles admin transfer 
            for x in accounts:
                if(int(x['account_number']) == self.account_num_from):
                    if(self.amount > int(x["balance"])): # Handles insufficent transfer amount
                        log_constraint_error("Balance Violation Error", "Insufficent balance")
                    else: # Handles transfer 
                        x["balance"] -= self.amount # Subtract from account to transfer from
                        
                        for y in accounts: # Subtracts from account to transfer to 
                            if(int(y['account_number']) == self.account_num_to):
                                y["balance"] += self.amount
                        write_new_current_accounts(accounts, file_path) # Writes to file
            
                else:
                    log_constraint_error("Account Violation Error", "Account does not exisit")

        else: # Handles standard transfer
            for x in accounts:
                if(int(x['account_number']) == self.account_num):
                    if(self.amount > 1000): # Handles standard user transfer limit
                        log_constraint_error("Withdrawl Limit Violation", "Standard user cannot withdraw above $1000")
                    
                    elif(self.amount > int(x["balance"])): # Handles insufficent transfer amount
                        log_constraint_error("Balance Violation Error", "Insufficent balance")

                    else:
                        x["balance"] -= self.amount # Subtract from account to transfer from

                        for y in accounts: # Subtracts from account to transfer to 
                            if(int(y['account_number']) == self.account_num_to):
                                y["balance"] += self.amount
                        write_new_current_accounts(accounts, file_path) # Writes to file
                else:
                    log_constraint_error("Account Violation Error", "Account does not exisit")