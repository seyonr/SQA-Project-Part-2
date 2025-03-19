from print_error import log_constraint_error

class ChangePlan:
    def __init__(self, account_num, is_admin):
        self.account_num = account_num
        self.is_admin = is_admin

    def change_plan(self):
        from read import read_old_bank_accounts

        file_path = ""  # Set to correct path file
        accounts = read_old_bank_accounts(file_path)  # Load all valid accounts

        account_found = False # Assume that account doesn't exist so that if for loop below doesn't trigger then resulting output would be a failure message 

        for x in accounts:
            if int(x['account_number']) == self.account_num:
                account_found = True # Don't want failure message to trigger when an actual valid account is found 

                if x["status"] == "D":  # Check if the account is disabled
                    log_constraint_error("Account Status Error", "Cannot change plan for a disabled account")
                    return

                # Toggle the plan type
                if x["account_plan"] == "student":
                    x["account_plan"] = "non-student"
                else:
                    x["account_plan"] = "student"

                print(f"Account {self.account_num} plan changed to {x['account_plan']}")
                return

        if not account_found:
            log_constraint_error("Account Violation Error", "Account does not exist")
