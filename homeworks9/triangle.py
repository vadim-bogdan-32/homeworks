class Triangle:
    def __init__(self, a, b,  c):
        if self.__check_if_exists(a, b, c):
            self.a = a
            self.b = b
            self.c = c

    def __check_if_exists(self, a, b, c,):

        if (a + b > c and a + c > b and b + c > a):
            return True
        raise ValueError("length of side must be less than sum of\
lengths of other two sides")

    def is_right_angled(self):

        sqa = self.a ** 2
        sqb = self.b ** 2
        sqc = self.c ** 2
        if (sqa == sqb + sqc or sqb == sqa + sqc or sqc == sqa + sqb):
            return True
        return False

    def get_perimeter(self):

        sum = self.a + self.b + self.c
        return sum

    def __eq__(self, other):

        if not isinstance(other, Triangle):
            raise TypeError("second argument must be Triangle")
        perimeter1 = self.get_perimeter()
        perimeter2 = other.get_perimeter()
        return perimeter1 == perimeter2


t1 = Triangle(3, 4, 5)
print(t1.is_right_angled())
try:
    t2 = Triangle(10, 10, 20)
except ValueError as e:
    print(e)
t3 = Triangle(11, 11, 20)
print(t3.is_right_angled())
print(t1 != t3)
