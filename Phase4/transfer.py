from print_error import log_constraint_error
from read import read_old_bank_accounts
from write import write_new_current_accounts

class Transfer:
    def __init__(self, amount, account_num_from, account_num_to, is_admin):
        self.amount = amount
        self.account_num_from = account_num_from
        self.account_num_to = account_num_to
        self.is_admin = is_admin

    # Pass the accounts data to another function or file
    def transfer(self):
        file_path = "" # Set to correct path file 
        accounts = read_old_bank_accounts(file_path) # Will hold all valid accounts
        
        if(self.is_admin): # Admin code handle 
            for x in accounts:
                if(int(x['account_number']) == self.account_num_from):
                    if(self.amount > int(x["balance"])):
                        log_constraint_error("Balance Violation Error", "Insufficent balance")
                    else:
                        x["balance"] -= self.amount

                        # Doing the acutal transfer
                        for y in accounts:
                            if(int(y['account_number']) == self.account_num_to):
                                y["balance"] += self.amount
                        write_new_current_accounts(accounts, file_path)
            
                else:
                    log_constraint_error("Account Violation Error", "Account does not exisit")

        else: # Standard user code handle
            for x in accounts:
                if(int(x['account_number']) == self.account_num):
                    if(self.amount > 1000):
                        log_constraint_error("Withdrawl Limit Violation", "Standard user cannot withdraw above $1000")
                    
                    elif(self.amount > int(x["balance"])):
                        log_constraint_error("Balance Violation Error", "Insufficent balance")

                    else:
                        x["balance"] -= self.amount

                        # Doing the acutal transfer
                        for y in accounts:
                            if(int(y['account_number']) == self.account_num_to):
                                y["balance"] += self.amount
                        write_new_current_accounts(accounts, file_path)
                else:
                    log_constraint_error("Account Violation Error", "Account does not exisit")