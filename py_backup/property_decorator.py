class Student(object):
    def __init__(self, **kwargs):
        self.name = kwargs['name']

    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError("score must be an integer!")
        if value < 0 or value > 100:
            raise ValueError("score must be between 0 ~ 100")
        self._score = value


class Celsius:
    """
    good resource: https://www.programiz.com/python-programming/property
    """

    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return self.temperature * 1.8 + 32

    @property
    def temperature(self):
        print("Getting value...")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible.")
        self._temperature = value

    # temperature = property(get_temperature, set_temperature)
    # temperature = property()
    # temperature = temperature.getter(get_temperature)
    # temperature = temperature.setter(set_temperature)
