# method to compute the temperature of water at equidistant time intervals and plot the result
def plot_water_heater_cooling(ambient_temp, initial_temp, time_in_hours):
    import matplotlib.pyplot as plt
    import numpy as np
    from water_heater import WaterHeater
    heater = WaterHeater(2000, 120)
    temp = []
    for t in np.arange(0, time_in_hours, 0.1):
        temp.append(heater.temperature(ambient_temp, initial_temp, t*3600))
    plt.plot(np.arange(0, time_in_hours, 0.1), temp)
    plt.xlabel('Time (hours)')
    plt.ylabel('Temperature (°C)')
    plt.show()

if __name__ == '__main__':
    plot_water_heater_cooling(20, 80, 48)
