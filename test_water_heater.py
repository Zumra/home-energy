# add a method to test the water heater class

import unittest
from water_heater import WaterHeater

class WaterHeaterTestCase(unittest.TestCase):
    def testEnergy(self):
        # arrange
        heater = WaterHeater(2000, 120)
        # act
        energy = heater.energy(10, 60)
        # assert
        self.assertAlmostEqual(energy, 7, 1)

if __name__ == '__main__':
    unittest.main()