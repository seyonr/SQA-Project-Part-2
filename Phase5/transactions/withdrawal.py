# Imports
from print_error import log_constraint_error
from read import read_old_bank_accounts
from update import update

class Withdrawal:
    # Default Constructor 
    def __init__(self, amount, account_num, is_admin):
        self.amount = amount
        self.account_num = account_num
        self.is_admin = is_admin

    # Function which handles the withdrawal logic itself
    def withdrawal(self):
        file_path = "accounts.txt" 
        accounts = read_old_bank_accounts(file_path) # Stores the accounts from the txt file 
        
        account_found = False  # Flag to track if an account is found

        if(self.is_admin): # Handles admin withdrawal
            for x in accounts:
                if(int(x['account_number']) == self.account_num): 
                    account_found = True  # Account found
                    if(self.amount > int(x["balance"])): # Handles insufficient balance withdrawal
                        log_constraint_error("Balance Violation Error", "Insufficient balance")
                    else: # Handles withdrawal from account
                        x["balance"] -= self.amount
                        x['total_transactions'] += 1
                        update(accounts, file_path)
                        return
    
            if not account_found:  # Log error once if account not found
                log_constraint_error("Account Violation Error", "Account does not exist")
        
        else: # Handles standard user withdrawal
            for x in accounts:
                if(int(x['account_number']) == self.account_num):
                    account_found = True  # Account found
                    if(self.amount > 1000): # Handles standard withdrawal limit
                        log_constraint_error("Withdrawl Limit Violation", "Standard user cannot withdraw above $1000")
                    elif(self.amount > int(x["balance"])): # Handles insufficient balance 
                        log_constraint_error("Balance Violation Error", "Insufficient balance")
                    else: # Handles withdrawal from account
                        x['total_transactions'] += 1
                        x["balance"] -= self.amount
                        update(accounts, file_path)
                        return
            
            if not account_found:  # Log error once if account not found
                log_constraint_error("Account Violation Error", "Account does not exist")
