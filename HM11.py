import math
"""1.Создайте класс Soda(газировка). Для инициализации есть параметр ,
которые определяет вкус газировки. При инициализации этот параметр
можно задвать , а можно и не задавать. Реализовать метод строковой
репрезентации , который возвращает строку вроде «У вас газировка с
<клубничным> вкусом , если вкус задан. Если вкус не задан метод должен
возрващать строку “У вас обычная газировка”"""

class Soda:
    def __init__(self, taste):
        self.taste = taste
    def gettaste(self):
        if self.taste:
            print (f'You have {self.taste}-flavored soda')
        else:
            print ('You have ordinary soda')

soda = Soda('')
soda.gettaste()

"""2.Напишите программу с классом Math. При инициализации атрибутов нет. 
Реализовать методы addition, subtraction,multiplication и division. При 
передаче в методы двух числовых параметров нужно производить с параметрами 
соответствующие действия и печатать ответ."""

class Math:
    def addition(self, a, b):
        result = a + b
        print (f'{a} + {b} = {result}')
    def subtraction(self, a, b):
        result = a - b
        print (f'{a} - {b} = {result}')
    def multiplication(self, a, b):
        result =  a * b
        print (f'{a} * {b} = {result}')
    def division(self, a, b):
        if b == 0:
            print("Error: division by zero")
        else:
            result =  a / b
            print (f'{a} / {b} = {result}')

m = Math()
m.addition(1, 2)
m.subtraction(6, 2)
m.multiplication(8, 2)
m.division(1, 5)
m.division(1, 0)


"""3.Программа с классом Car. При инициализации объекта ему должны задаваться
 атрибуты color,type и year. Реализовать пять методов. Запуск автомобиля – 
 выводит строку «Автомобиль заведен». Отключение авто – выводит строку 
 «Автомобиль заглушен». Методы для присовения авто годы выпускаб типа и цвета"""

class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def start(self):
        print (f'Engine launch')

    def stop(self):
        print (f'Engine stop')

    def set_color(self, color):
        self.color = color

    def set_type(self, type):
        self.type = type

    def set_year(self, year):
        self.year = year

    def info(self):
        print (f'Car: {self.color}, {self.type}, {self.year}')

car1 = Car('red', 'Sedan', 1999)
car1.start()
car1.stop()
car1.set_color('blue')
car1.set_type('Sub')
car1.set_year(2025)
car1.info()

"""4. Программа с классом Sphere для предоставления сферы в трехмерном пространстве"""

class Sphere:
    def __init__(self, radius=1, x=0, y=0, z=0):
        self.radius = radius
        self.x = x
        self.y = y
        self.z = z

    def get_volume(self):
        return 4/3 * 3.14 * (self.radius ** 3)

    def get_radius(self):
        return self.radius

    def get_square(self):
        return 4 * 3.14 * (self.radius ** 2)

    def set_radius(self, radius):
        self.radius = radius

    def set_center(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def is_point_inside_sphere(self, x, y, z):
        point = math.sqrt((x - self.x) **2 + (y - self.y) **2 + (z - self.z) **2)
        return point <= self.radius

s1=Sphere(3,1,2,5)
s2=Sphere()
s3=Sphere(7)

s3.set_center(1,2,3)
s2.set_radius(4)
s1.is_point_inside_sphere(1,2,3)

print(s1.get_volume())
print(s3.get_square())
print(s1.is_point_inside_sphere(1,2,3))
print(s3.get_radius())
print(s2.get_radius())

"""5. Разработать класс SuperStr, который наследует функциональность 
стандартного типа str и содержит два новых метода"""

class SuperStr(str):
    def is_repeatance(self, s):
        if not s:
            return False
        if len(self) % len(s) != 0:
            return False
        return self == s *(len(self)//len(s))

    def is_palindrome(self):
        s = self.lower()
        return s == s[::-1]

a = SuperStr('ftftft')
print(a.is_repeatance('ft'))
print(a.is_repeatance('sss'))

b = SuperStr('fbccbf')
print(b.is_palindrome())
print(SuperStr('').is_palindrome())
print(SuperStr('Marko').is_palindrome())
