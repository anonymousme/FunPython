def recursive_factorial(n):

    if n<=1:
       return 1
    else:
       
        return n * recursive_factorial(n-1)
        

    
def iterative_factorial(n):
   
    i  = 1 
    prod = 1 
    while i <=n:
        
        prod = prod * i
        
        i=i+1
    
    return prod


import unittest

class RecursiveTestCase(unittest.TestCase):

  def test_recursive_factorial_one(self):
    result = recursive_factorial(4)
    self.assertEqual(result, 24, msg="Inaccurate value")
  
  def test_recursive_factorial_two(self):
    result = recursive_factorial(0)
    self.assertEqual(result, 1, msg="Inaccurate value")
  
  def test_iterative_factorial_one(self):
    result = iterative_factorial(5)
    self.assertEqual(result, 120, msg="Inaccurate value")
    
  def test_iterative_factorial_two(self):
    result = iterative_factorial(12)
    self.assertEqual(result, 479001600, msg="Inaccurate value")

if __name__=="__main__":
    unittest.main()


