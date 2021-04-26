class Roi: 
    def __init__(self):
        self.values = {}
    
    def getIncome(self): 
        rental = int(input("Whats your rental income: ?"))
        self.rental = rental 
        
        laundry = int(input("Laundry Cost"))
        self.laundry = laundry

        storage = int(input (" Storage Cost"))
        self.storage = storage 

        misc = int(input(" Now enter any MISC costs: "))
        self.misc = misc

        total_income = int(rental + misc + laundry + storage)
        self.total_income = total_income
        print("Your total income is:", total_income)
        return total_income

    def getExpense(self): 
        tax = input("Whats your tax payment on property? ")
        self.tax = tax
        
        insurance = input("Whats your insurance amount for the property?")
        self.insurance = insurance 

        utilities = input("Enter all utilities cost including Electric/ Water/ Sewer / Gass/ Garbage: ")
        self.utilities = utilities

        vacancy = input("What's your vacancy cost for the property: ")
        self.vacancy = vacancy

        repairs = input("Whats your total repair cost paid?")
        self.repairs = repairs

        prop_morg = input("Whats the mortgage on the property?: ")
        self.prop_morg = prop_morg

        morg = input("Whats the current mortgage payment: ")
        self.morg = morg

        total_expense = int(tax + insurance + utilities + vacancy + repairs + prop_morg + morg)
        self.total_expense = total_expense

        print("Your total expense is: " , total_expense)
        return total_expense

    def cashFlow(self, total_income, total_expense): 
        
        cash_flow = int(total_income - total_expense)
        self.cash_flow = cash_flow 
        print("Your total cash flow is: " , cash_flow)

    def CashOnCash(self, cash_flow, total_investment):
        down_payment = int(input ("How much down payment did you put: "))
        self.down_payment = down_payment

        closing_cost = int(input("How much did you pay for closing cost: "))
        closing_cost = self.closing_cost

        rehab_budget = int(input ("Enter the amount spent on rehab: "))
        rehab_budget = self.rehab_budget

        total_investment = int(down_payment + closing_cost + rehab_budget) 
        self.total_investment = total_investment
        print("Your total investement put on this property is: ", total_investment)

        cash_roi = (cash_flow * 12) / total_investment
        self.cash_roi = cash_roi
        print("Your ROI on this property is going to be: ", cash_roi)

a = Roi()
b = Roi()
c = Roi() 
d = Roi()

print("Welcome to my ROI Calculator")
a.getIncome()
b.getExpense()
c.cashFlow(total_income, total_expense) # i cant pass my local variables used in the first two functions to be used in another function...
d.CashOnCash()