def get_algorithm_result(num_list):
    if type(num_list) == type([]):
        Largest = num_list[0]
        for item in range(0,len(num_list)):
            if Largest < num_list[item]:
                Largest = num_list[item]
        return Largest
             


def prime_number(integer):
  if integer == 1:
    return False
  elif integer == 3:
    return True
  if integer > 3:
    for i in range(3, (integer-1)):
      if integer % i == 0:
        return False
      else:
        return True
            
            

    
         
import unittest

class AlgorithmTestCases(unittest.TestCase):
  def test_maximum_number_one(self):
    result = get_algorithm_result([1, 78, 34, 12, 10, 3])
    self.assertEqual(result, 78, msg="Incorrect number")
    
  def test_maximum_number_two(self):
    result = get_algorithm_result(["apples", "oranges", "mangoes", "banana", "zoo"])
    self.assertEqual(result, "zoo", msg="Incorrect value")

  def test_prime_number_one(self):
    result = prime_number(1)
    self.assertEqual(result, False, msg="Result is invalid")

  def test_prime_number_two(self):
    result = prime_number(78)
    self.assertEqual(result, False, msg="Result is invalid")
    
  def test_prime_number_three(self):
    result = prime_number(11)
    self.assertEqual(result, True, msg="Result is invalid")
if __name__=="__main__":
    unittest.main()
