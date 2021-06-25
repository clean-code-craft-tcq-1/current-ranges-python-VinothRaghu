# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 07:26:48 2021

@author: VNO1COB
"""
import unittest
import bms_reading

class test_battery_management_continous_current_reading(unittest.TestCase):
    
  def test_battery_current_not_in_range(self):
    self.assertTrue(bms_reading.current_ranges([]) == "Wrong Input")  # Failing test case
    
  def test_valid_current_ranges(self):
    self.assertTrue(bms_reading.current_ranges([3, 3, 4, 7 ,10, 11, 12, 13]) == "Correct Input") 
    
  def test_valid_current_ranges_less_reading(self):
    self.assertTrue(bms_reading.current_ranges([3, 3, 4, 7]) == "Correct Input") 

  def test_wrong_current_ranges(self):
    self.assertTrue(bms_reading.current_ranges([3,4,5,6,7,8]) == "Wrong Input")    #There is no constant range
    

if __name__ == '__main__':
  unittest.main()