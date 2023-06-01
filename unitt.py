# def test_case_one():
#     assert 50 *10 == 500 , "should be 500"
# def test_case_two():
#     assert 10 <20 ,"should be true"
# if __name__ == "__main__":
#         test_case_one()
#         test_case_two()
#         print("all is done")

import unittest
class mytestcase(unittest.TestCase):
    def test_one(self):
        self.assertTrue(20 <10,"should be true")
    def test_two(self):
        self.assertEqual(20+10,30,"should be 30")
if __name__ == "__main__":
    unittest.main()
    