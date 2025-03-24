# Import
from login import Login
from withdrawal import Withdrawal
from transfer import Transfer
from paybill import Paybill
from deposit import Deposit
from create import Create
from delete import Delete
from disable import Disable
from changeplan import ChangePlan

# Class which calls instance of all classes 
class TransactionHandler:
    def __init__(self, amount = 0, account_num = 0, account_name = "", account_num_to = 0, status = "", plan = "", is_admin = False):
        self.amount = amount
        self.account_num = account_num
        self.account_name = account_name
        self.account_num_to = account_num_to
        self.status = status
        self.plan = plan
        self.is_admin = is_admin

    def login_handle(self):
        login_instance = Login(self.account_num, self.account_name, self.is_admin)
        login_instance.login()
    
    def withdrawal_handle(self):
        withdrawal_instance = Withdrawal(self.amount, self.account_num, self.is_admin)
        withdrawal_instance.withdrawal()
    
    def transfer_handle(self):
        transfer_instance = Transfer(self.account_num, self.account_num_to, self.is_admin)
        transfer_instance.transfer()

    def paybill_handle(self):
        paybill_instance = Paybill(self.amount, self.account_num, self.is_admin)
        paybill_instance.paybill()

    def deposit_handle(self):
        deposit_instance = Deposit(self.amount, self.account_num, self.is_admin)
        deposit_instance.deposit()

    def create_handle(self):
        create_instance = Create(self.amount, self.account_num, self.account_name, self.status, self.is_admin, self.plan)
        create_instance.create()

    def delete_handle(self):
        delete_instance = Delete(self.account_num, self.is_admin)
        delete_instance.delete()

    def disable_handle(self):
        disable_instance = Disable(self.account_num, self.is_admin)
        disable_instance.disable()

    def changeplan_handle(self):
        changeplan_instance = ChangePlan(self.account_num, self.is_admin)
        changeplan_instance.change_plan()