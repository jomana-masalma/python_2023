#TASK 1 : #Create a class named Car and let class have brand, model name, construction year as attributes

class Car:
    def __init__(self, brand, model_name, construction_year):
        self.brand = brand
        self.model_name = model_name
        self.construction_year = construction_year
jomana_car = Car("BMW", "GT", 2020)
print(jomana_car.brand)  # Output:  BMW
print(jomana_car.model_name)  # Output:GT
print(jomana_car.construction_year)  # Output: 2020


# TASK 2: Create an Object of the car class and name it car1 with the brand porsche, the model cayenne and a construction year of 2019
car1=Car("porsche", "Cayenne", 2019 )
print(car1.brand)
print(car1.model_name)
print(car1.construction_year)


#TASK 3: Give the class a constructor(__init__) and repr(__rep__) function and use the repr function to print out the attributes

class Car :
    def __init__(self, brand, model_name, construction_year):
        self.brand= brand
        self.model_name= model_name
        self.construction_year= construction_year

    def __repr__(self):
        return f"Car(brand={self.brand}, model_name={self.model_name}), construction_year={self.construction_year})"
Car1 = Car("porsche","Cayenne", 2019)
print(Car1)





