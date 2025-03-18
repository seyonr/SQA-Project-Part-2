from print_error import log_constraint_error

class Deposit:
    def __init__(self, amount, account_num, is_admin, plan):
        self.amount = amount
        self.account_num = account_num
        self.is_admin = is_admin
        self.plan = plan

    def deposit(self):
        from read import read_old_bank_accounts
        from write import write_new_current_accounts

        file_path = ""  # Set to correct path file
        accounts = read_old_bank_accounts(file_path)  # Will hold all valid accounts

        if(self.is_admin): # Admin code handle
            for x in accounts:
                if(int(x['account_number']) == self.account_num):
                    if("NP" == self.plan):
                        x["balance"] += self.amount - 0.1  # Deducting 10 cents for "non-student" plan
                    elif("SP" == self.plan):
                        x["balance"] += self.amount - 0.05 # Deducting 5 cents for "student" account.
                    write_new_current_accounts(accounts, file_path)
                    return
                else:
                    log_constraint_error("Account Violation Error", "Account does not exisit")
        else:
            for x in accounts:
                if(int(x['account_number']) == self.account_num):
                    if ("NP" == self.plan):
                        x["balance"] += self.amount - 0.1  # Deducting 10 cents for "non-student" plan
                    elif ("SP" == self.plan):
                        x["balance"] += self.amount - 0.05  # Deducting 5 cents for "student" account.
                    write_new_current_accounts(accounts, file_path)
                else:
                    log_constraint_error("Account Violation Error", "Account does not exisit")
