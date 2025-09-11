import json
from gui import *
class Customer:
    def __init__(self,acc_no,paswrd):
        self.acc_no=acc_no
        self.password=paswrd


    def Money_deposit(self,amount):
        with open("Customer_data.json", "r") as data:
            fin_data = json.load(data)
        if self.acc_no in fin_data:
            fin_data[self.acc_no]["balance"] =int(fin_data[self.acc_no]["balance"])+int(amount)
        with open("Customer_data.json","w") as data:
            json.dump(fin_data,data,indent=4)
        return True



    def Money_withdraw(self,amount):
        with open("Customer_data.json", "r") as data:
            fin_data = json.load(data)
        if self.acc_no in fin_data:
            fin_data[self.acc_no]["balance"] =int(fin_data[self.acc_no]["balance"])-int(amount)
        with open("Customer_data.json","w") as data:
            json.dump(fin_data,data,indent=4)
        return True


    def account_status(self):
        pass


    def account_balance(self):
        pass

cust=Customer(456,"hello")
cust.Money_deposit(78)