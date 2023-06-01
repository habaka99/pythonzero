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
    print("".join(serial_list))
make_serial(61)