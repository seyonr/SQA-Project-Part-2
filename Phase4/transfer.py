# Imports
from print_error import log_constraint_error
from read import read_old_bank_accounts
from write_master import write_master_bank_accounts

class Transfer:
    # Constructor 
    def __init__(self, amount, account_num_from, account_num_to, is_admin):
        self.amount = amount
        self.account_num_from = account_num_from
        self.account_num_to = account_num_to
        self.is_admin = is_admin

    # Function which handles transfer
    def transfer(self):
        file_path = "accounts.txt" # Will be set to the path of the file itself
        accounts = read_old_bank_accounts(file_path) # Stores the accounts from the txt file 

        if(self.is_admin): # Handles admin transfer
            from_account_found = False # Will prevent constant logging of "Account not existing"
            for x in accounts:
                if (int(x['account_number']) == self.account_num_from):
                    from_account_found = True
                    if(self.amount > int(x["balance"])): # Handles insufficent transfer amount
                        log_constraint_error("Balance Violation Error", "Insufficent balance")
                    else: # Handles transfer 
                        x["balance"] -= self.amount # Subtract from account to transfer from

                        for y in accounts: # Subtracts from account to transfer to 
                            if(int(y['account_number']) == self.account_num_to):
                                y["balance"] += self.amount
                        write_master_bank_accounts(accounts, file_path) # Writes to file
                    break
            
            if not from_account_found:
               log_constraint_error("Account Violation Error", "Account does not exisit")

        else: # Handles standard transfer
            from_account_found = False
            for x in accounts:
                if(int(x['account_number']) == self.account_num_from):
                    from_account_found = True
                    if(self.amount > 1000): # Handles standard user transfer limit
                        log_constraint_error("Transfer Limit Violation", "Standard user cannot transfer above $1000")
                    
                    elif(self.amount > int(x["balance"])): # Handles insufficent transfer amount
                        log_constraint_error("Balance Violation Error", "Insufficent balance")

                    else:
                        x["balance"] -= self.amount # Subtract from account to transfer from

                        for y in accounts: # Subtracts from account to transfer to 
                            if(int(y['account_number']) == self.account_num_to):
                                y["balance"] += self.amount
                        write_master_bank_accounts(accounts, file_path) # Writes to file
                    break
            if not from_account_found:
                log_constraint_error("Account Violation Error", "Account does not exisit")

