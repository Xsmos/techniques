class Dog():
    """
    模拟小狗
    """

    def __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗蹲下"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """模拟小狗打滚"""
        print(self.name.title() + " rolled over!")


class Car():
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """打印汽车里程"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cannot roll back an odometer!")

    def increment_odometer(self, miles):
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You cannot increase negative odometer!")


class Battery():
    """电车的电瓶"""
    def __init__(self, battery_size = 70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This electric car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        range = self.battery_size*10

        message = "This ecar can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)


class ElectricCar(Car):
    """电动汽车继承了汽车的属性和方法"""
    def __init__(self, make, model, year):
        """初始化父类属性"""
        super().__init__(make, model, year)
        self.battery = Battery(80)

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This electric car has a " + str(self.battery.battery_size) + "-kWh battery.")

    def read_odometer(self):
        """打印电车里程"""
        print("This electric car has " + str(self.odometer_reading) + " miles on it.")

