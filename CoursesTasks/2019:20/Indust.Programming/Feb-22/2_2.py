import unittest

def plus(a, b):
    try:
        a = int(a)
    except:
        print("Cant convert a to int")
        exit(1)
    try:
        b = int(b)
    except:
        print("Cant convert a to int")
        exit(1)
    return a + b

class Mytests(unittest.TestCase):
    def test_plus(self):
        res = plus(1, 3)
        self.assertEqual(res, 4)

    def test_big_num(self):
        res = plus(9223372036854775807, 9223372036854775807)
        self.assertEqual(res, 18446744073709551614)
    
    def test_very_big_num(self):
        res = plus(18446744073709551615, 18446744073709551615)
        self.assertEqual(res, 36893488147419103230)

    def test_string2int(self):
        res = plus("1", "3")
        self.assertEqual(res, 4)
    def test_str(self):
        self.assertEqual(plus("1", "a"), 3)
    

if __name__ == '__main__':
    a,b = map(int,input().split(' '))
    print(int(plus(a,b)))
    #unittest.main()
