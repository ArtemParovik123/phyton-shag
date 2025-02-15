class Human:
    def __init__(self, name, house, car=None, job=None):
        self.name = name
        self.house = house
        self.car = car
        self.job = job
        self.money = 1000
        self.gladness = 50
        self.odezda = 20
        self.produkti = 30
        
    def shoping(self):
        if odezda < 5:
            print("Поїхав за одежою")
            odezda += 10
        elif produkti < 10
            print("Поїхав за Їжою")
        
    def work(self):
        pass
    
    def eat(self):
        pass
    
    def chill(self):
        pass
    
    def cleaning(self):
        pass
    
    def live(self):
        pass
    
    def is_alive(self):
        if self.money <0:
            return False
        return True
    
    
class Car:
    def __init__(self, model):
        self.model = model
        self.fuel = 60
        self.state = 100
        
    def drive(self, length):
        rashod = lenngth * 0.1
        if self.fuel - rashod < 0:
            print("Подорож не можлива, не вистачає пального")
        else:
            self.fuel -= rashod
            self.state -= lenght * 0.01
            print(f"Ми проїхали {length} км, витратили{rashod} літрів пального")
            
    def add_fuel(self, fuel):
        if self.fuel + fuel <= 60:
            self.fuel += fuel
            print("Ми заправили {fuel}л мального")
        else:
            self.fuel = 60
            print("Бак повний!")
            
            
    def __str__(self):
        pass

class Job:
    def __init__(self, name, salsry):
        self.name = name
        self.salary = salary
    
    def __str__(self):
        return f"Робота: {self.name},зарплата - {self.salary}$"

class House:
    def __init__(self):
        self.pollution = 0
        self.food = 0
    
    def __str__(self):
        print(f"Будинок: запас їжі - {self.food}, забрудненість - {self.pollution}")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    