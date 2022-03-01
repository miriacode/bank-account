from BankAccount import BankAccount

#Create 2 accounts
miriam_account = BankAccount(0.02,3000)
rosa_account = BankAccount(0.03,2000)

miriam_account.deposit(1000).deposit(1000).deposit(1500).withdraw_money(500).generate_int().show_account_info()
rosa_account.deposit(2000).deposit(1000).withdraw_money(500).withdraw_money(1000).withdraw_money(500).withdraw_money(1000).generate_int().show_account_info()

BankAccount.print_account()