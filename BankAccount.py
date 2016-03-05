import unittest

class BankAccount(object):
  
  def __init__(self, balance):
    
    self.balance = balance
    
  def deposit(self,amount):
    
    self.balance = self.balance + amount
    return self.balance
     
  def withdraw(self,amount):
    
    if amount > self.balance:
      
      return "invalid transaction"
      
    else:
      
      self.balance = self.balance - amount
      
      return self.balance
      

class MinimumBalanceAccount(BankAccount):

  def __init__(self):
    self
    
    #self.balance =  balance


''' Test class'''
class AccountBalanceTestCases(unittest.TestCase):
  def setUp(self):
    self.my_account = BankAccount(90)
    
  def test_balance(self):
    self.assertEqual(self.my_account.balance, 90, msg='Account Balance Invalid')
    
  def test_deposit(self):
    self.my_account.deposit(90)
    self.assertEqual(self.my_account.balance, 180, msg='Deposit method inaccurate')
    
  def test_withdraw(self):
    self.my_account.withdraw(40)
    self.assertEqual(self.my_account.balance, 50, msg='Withdraw method inaccurate')
    
  def test_invalid_operation(self):
    self.assertEqual(self.my_account.withdraw(1000), "invalid transaction", msg='Invalid transaction')
  
  def test_sub_class(self):
    self.assertTrue(issubclass(MinimumBalanceAccount, BankAccount), msg='No true subclass of BankAccount')
    
if __name__=="__main__":
    unittest.main()
