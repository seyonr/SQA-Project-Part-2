# Import 
from print_error import log_constraint_error
from read import read_old_bank_accounts
from write_master import write_master_bank_accounts

class Create:
    # Constructor 
    def __init__(self, amount, account_name, status, is_admin, plan):
        self.amount = amount
        self.account_name = account_name
        self.status = status
        self.is_admin = is_admin
        self.plan = plan

    def create(self):
        file_path = "accounts.txt"
        accounts = read_old_bank_accounts(file_path)

        if self.is_admin:
            # Getting a set of used account numbers 
            existing_numbers = {int(acc['account_number']) for acc in accounts}

            # Generate a new account number 
            for num in range(1, 100000):
                if num not in existing_numbers:
                    unique_account_number = str(num).zfill(5)
                    break
            else:
                log_constraint_error("Account Creation Error", "No available account numbers.")
                return

            # Create new account with unique account number
            accounts.append({
                'account_number': unique_account_number,
                'name': self.account_name,
                'status': self.status,
                'balance': self.amount,
                'total_transactions': 0,
                'plan': self.plan
            })

            write_master_bank_accounts(accounts, file_path)
        else:
            log_constraint_error("Unprivileged User Error", "Standard user does not have admin privileges")
