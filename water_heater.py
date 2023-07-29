import math


class WaterHeater:
    def __init__(self, power, volume):
        self.power = power
        self.volume = volume
        self.mass = self.volume * 1000
        self.specific_heat = 4.186

# The formula to calculate energy is mass * temperature difference * specific heat capacity.
# The specific heat capacity of water is 4.186 Joules / gram °C
# The temperature difference is the difference between the desired temperature and the initial temperature.
# The initial temperature is the temperature of the water before the heater turns on.
# The desired temperature is 37°C.
# The mass of the water is the number of liters * 1000. (e.g. 50 liters = 50,000 grams)
    def energy(self, initial_temp, desired_temp):
        tempDiff = desired_temp - initial_temp
        energy_in_joules = self.mass * tempDiff * self.specific_heat
        energy_in_kwh = energy_in_joules / 3600000
        return energy_in_kwh

# method based on Newton's law of cooling which computes the temperature of water after a certain amount of time
# The formula to calculate temperature is: temperature = ambient + (initial - ambient) * e^(-kt)
# The ambient temperature is the temperature of the water surrounding the heater.
# The initial temperature is the temperature of the water before the heater turns on.
    def temperature(self, ambient_temp, initial_temp, time):
        k = 0.0000192
        temperature = ambient_temp + (initial_temp - ambient_temp) * math.exp(-k * time)
        return temperature