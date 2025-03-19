from print_error import log_constraint_error
class Create:
    def __init__(self, amount, account_num, account_name,status, is_admin, plan):
        self.amount = amount
        self.account_num = account_num
        self.account_name = account_name
        self.status = status
        self.is_admin = is_admin
        self.plan = plan

    def create(self):
        from read import read_old_bank_accounts
        from write import write_new_current_accounts

        file_path = ""  # Set to correct path file
        accounts = read_old_bank_accounts(file_path)  # Load all valid accounts

        # Adding new account to file
        if self.is_admin:
            accounts.append({
                'account_number' : self.account_num,
                'name': self.account_name,
                'status': self.status,
                'balance': self.amount,
                'total_transactions': 0
            })
            write_new_current_accounts(accounts, file_path)
        else:
            log_constraint_error("Unprivileged User Error", "User does not have admin privileges")