# Imports
from print_error import log_constraint_error
from read import read_old_bank_accounts
from write_master import write_master_bank_accounts

class Withdrawal:
    # Default Constructor 
    def __init__(self, amount, account_num, is_admin):
        self.amount = amount
        self.account_num = account_num
        self.is_admin = is_admin

    # Function which handles the withdrawal logic itself
    def withdrawal(self):
        file_path = "accounts.txt" # Will be set to the path of the file itself
        accounts = read_old_bank_accounts(file_path) # Stores the accounts from the txt file 
        
        if(self.is_admin): # Handles admin withdrawal
            for x in accounts:
                if(int(x['account_number']) == self.account_num): 
                    if(self.amount > int(x["balance"])): # Handles insufficent balance withdrawal
                        log_constraint_error("Balance Violation Error", "Insufficent balance")
                    else: # Handles withdrawal from account
                        x["balance"] -= self.amount
                        x['total_transactions'] += 1
                        write_master_bank_accounts(accounts, file_path) # Writes to file
    
                else:
                    log_constraint_error("Account Violation Error", "Account does not exisit")

        else: # Handles standard withdrawal
            for x in accounts:
                if(int(x['account_number']) == self.account_num):
                    if(self.amount > 1000): # Handles stanard withdrawal limit
                        log_constraint_error("Withdrawl Limit Violation", "Standard user cannot withdraw above $1000")
                    elif(self.amount > int(x["balance"])): # Handles insufficent balance 
                        log_constraint_error("Balance Violation Error", "Insufficent balance")
                    else: # Handles withdrawal from account
                        x["balance"] -= self.amount
                        write_master_bank_accounts(accounts, file_path) # Writes to file
                else:
                    log_constraint_error("Account Violation Error", "Account does not exisit")