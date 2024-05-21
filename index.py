# SOLID
# S - single responsibility principle - принцип единой ответственности
# О - Open-closed principle - принцип открытости-закрытости: Можем добавлять новый функционал, не меняя старый
# L - Liskov Substitution principle - принцип замещения лисков - можем класс-наследник подставить в любое место
# программы вместо родительского и ничего не сломается.
# I - Interference segregation principle - Принцип разделения интерфейсов - клиент не должен реализовывать интерфейс,
# который он не собирается использовать
# D - Dependency Inversion principle - Принцип инверсии зависимостей - есть машина и колесо. Если колесо мишлен - то
# машина работает уже с конкретным колесом, а не абстрактным.

#S
class User:
    def __init__(self, db_conn, name, surname):
        self.db = db_conn
        self.name = name
        self.surname = surname

    def get_name(self):
        return self.name


class UserModelDB:
    def get_username(self, user):
        pass
    def save_db(self, user):
        pass

class FileManager:
    def read_file(self, filename): #читсается дата
        pass

    def write_file(self, filename):
        pass

class DataProcessor:
    def process_data(self, data): #обработка
        pass

class ReportGenerator:
    def generate_report(self, data): #создается какой-то отчет
        pass

#O

class Discount:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def give_discount(self):
        return self.price * 0.2

    #появилась необходимость добавить вип скидку
class VipDiscount(Discount):
    def get_discount(self):
        return super().give_discount() * 2

#L

class Vehicle:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def get_name(self):
        return self.name

    def speed(self):
        return self.speed

    def engine(self):
        pass

    def start_engine(self):
        self.engine()

# class Car(Vehicle):
#     def start_engine(self):
#         pass
#
# class Bicycle(Vehicle):
#     def start_engine(self):
#         pass

class VehicleWithoutEngine(Vehicle):
    def start_moving(self):
        pass

class VehicleWithEngine(Vehicle):
    def engine(self):
        pass
    def start_engine(self):
        pass

class Car(VehicleWithEngine):
    def start_engine(self):
        pass

class Bicycle(VehicleWithoutEngine):
    def start_engine(self):
        pass



#I - у нас есть фигура, 2 метода: нарсовать круг и нарисовать квадрат. Встает вопрос зачем кругу рисовать квадрат?

class Shape:
    def draw_circle(self):
        pass
    def draw_square(self):
        pass

class Circle(Shape):
    def draw_circle(self):
        pass
    def draw_square(self):
        pass

#ПЕРЕПИШЕМ ПРАВИЛЬНО:

class Shape:
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        pass

class Square(Shape):
    def draw(self):
        pass



#D - Принцип инверсии зависимостей - есть машина и колесо. Если колесо мишлен - то
# машина работает уже с конкретным колесом, а не абстрактным. Нельзя создавать какие-то зависимости в классе.


class LightBulb:
    def turn_on(self):
        print('Яркая лампочка включена')

class LightSwitch: # Класс выключатель, у него есть атрибут лампочка
    def __init__(self):
        self.light_bulb = LightBulb() #сюда присвоили объект LightBulb и LightSwitch зависит от LightBulb - так
        # нельзя. Нерпавильный вариант

    def toggle(self): #метод для включения
        print("Toggle the light switch")
        self.light_bulb.turn_on()

#Правильный вариант:

class Switchable:
    def turn_on(self):
        pass

class LightBulb(Switchable):
    def turn_on(self):
        print("Яркая лампа включена")

class LightSwitch:
    def __init__(self, swithchable_devices):
        self.swithchable_devices = swithchable_devices

    def toggle(self):
        print("Toggle the light switch")
        self.swithchable_devices.turn_on()



#ЗАДАНИЕ НА КЛАССЫ

class Animal:
    def __init__(self, name, view, breed):
        self.name = name
        self.view = view
        self.breed = breed

    def get_name(self):
        return self.name


class Dog(Animal):
    def __init__(self, name, view, breed, speak):
        super().__init__(name, view, breed)
        self.speak = speak

    def get_name(self):
        super().get_name()

class Snake(Animal):
    def __init__(self, name, view, breed):
        super().__init__(name, view, breed)

    def get_name(self):
        super().get_name()

class Spider(Animal):
    def __init__(self, name, view, breed):
        super().__init__(name, view, breed)

    def get_name(self):
        super().get_name()
