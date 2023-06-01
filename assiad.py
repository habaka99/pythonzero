# import unittest
# class TestIn(unittest.TestCase):
#     def Test1(self):
#         self.assertIn(1, [1, 2, 3])
#     def test_in_list(self):
#         self.assertIn(1, [1, 2, 3])
#     def test2(self):
#         self.assertEqual(type(10),int,"The Type Of 10 Is Int")
# if __name__ =="__main__":
#      unittest.main()
# # import unittest


# # class TestIn(unittest.TestCase):
# #     def test_in_list(self):
# #         self.assertIn(1, [1, 2, 3])

# #     def test_in_string(self):
# #         self.assertIn('python', 'python tutorial')
# # if __name__ =="__main__":
# #    unittest.main()
import string
import random
def make_serial(count):
    all_chars=string.ascii_letters+string.digits
    # print(all_chars)
    chars_count=len(all_chars)
    serial_list=[]
    while count>0:
        ranom_num=random.randint(0,chars_count-1)
        random_chars=all_chars[ranom_num]
        serial_list.append(random_chars)
        count-=1
    for i in (4,10):
        serial_list[i] = '-' + serial_list[i]
    print((serial_list))
make_serial(14)