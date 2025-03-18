from print_error import log_constraint_error

class Delete:

    def __init__(self, amount, account_num, is_admin, plan):
        self.amount = amount
        self.account_num = account_num
        self.is_admin = is_admin
        self.plan = plan


    def delete(self):
        from read import read_old_bank_accounts
        from write import write_new_current_accounts


        file_path = ""  # Set to correct path file
        accounts = read_old_bank_accounts(file_path) 
        
        if(self.is_admin): # Admin code handle
            # i is the index and x is the account at each element of the dictionary. -> Enumerate prevents the for loop from being a tuple
            for i, x in enumerate(accounts):
                if(int(x['account_number']) == self.account_num):
                    accounts.pop(i)
                write_new_current_accounts(accounts, file_path)
                return
        else:
            log_constraint_error("Account Violation Error", "Account does not exisit")

