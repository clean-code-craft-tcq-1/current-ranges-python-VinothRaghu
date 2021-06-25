# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 07:58:40 2021

@author: VNO1COB
"""
def current_ranges(range_list):   
  if validate_input(range_list):
      list_tuple = []
      while len(range_list)>1:
          sequence_list,range_list = range_identifier(range_list)
          append_to_list(sequence_list,list_tuple)
      get_output(list_tuple)
      return 'Correct Input'
  return 'Wrong Input'       
    

def get_list(range_list,sequence,count):
    newRangeList = []    
    if (len(range_list) - count)> 0:
        newRangeList = range_list[count:]    
    return sequence,newRangeList           

def range_identifier(range_list):
    count = 0 
    sequence = []      
    for i in range_list:          
      if len(sequence) == 0:
        sequence.append(i)
        count+= 1
      elif i == sequence[count - 1] or i == (sequence[count - 1])+1:
        sequence.append(i)
        count+= 1
      else: 
        break
    sequence,newRangeList = get_list(range_list,sequence,count)
    return sequence,newRangeList
             
                    
def append_to_list(sequence_list,list_tuple):
    if len(sequence_list) > 1:              
        return(list_tuple.append(sequence_list))
  
def validate_input(ranges):
    return (len(ranges)>0)

def get_output(list_tuple):
    print('Ranges','Readings')
    for lst in list_tuple:
        reading = len(lst)
        ranges = str(lst[0]) + '-' + str(lst[len(lst) - 1])
        output = str(ranges) + ',' + str(reading)
        print(output)
    return output