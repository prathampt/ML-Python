import Simple_Banking_System_using_OOPS as b

parth = b.CurrentAccount("Parth", 10000, 50000000)
print(parth.get_balance())
pratham = b.SavingsAccount("Pratham", 348579287509, 5)
pratham.add_interest()
print(pratham.get_balance())