class Customer:
    def __init__(self,id,name):
        self.id = id
        self.name = name

    def customer_info(self):
        print(f'Customer id: {self.id} Name: {self.name}')

class Bill:
    customer = ""
    def __init__(self,bill_id,Customer,total):
        self.bill_id = bill_id
        self.customer = Customer
        self.total = total

    def display_bill(self):
        print(f'Bill ID: {self.bill_id} \n'
              f'Customer ID: {self.customer.id} Name: {self.customer.name}\n'
              f'Total: {self.total}')

#create objects
c1 = Customer("c001","Sam")
bill = Bill("b001",c1,5000)

#display info
c1.customer_info()
bill.display_bill()
