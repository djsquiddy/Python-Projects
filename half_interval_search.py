# Name: Dylan Jones
# Program: half interval search
# File: half_interval_search.py
# Date: 13/1/2013

import math

#function prototypes
def interval_search(function, neg_point, pos_point) : pass
def test_new_mid_point(function, neg_point, pos_point, mid_point) : pass
def function_value_less_than_tolerance(function, function_value, neg_point, pos_point, mid_point) : pass
def function_value_greater_than_tolerance(function, function_value, neg_point, pos_point, mid_point) : pass
def poly_01(x) : pass
def poly_02(x) : pass
def poly_03(x) : pass
def poly_04(x) : pass
def average(a, b) : pass

#global variable for the range of tolerance
tolerance_range = 0.000000001

#returns the average value of two variables
def average(a, b) : return abs(a + b) / 2.0

#return if the tolerance range has been meet
def is_small_enough(neg_point, pos_point) :
  tolerance = abs(neg_point - pos_point) / 2.0
  return tolerance <= tolerance_range

#finds the value of which a given function equals zero
#on an interval of [a,b] 
def interval_search(function, neg_point, pos_point) :
  mid_point = average(neg_point, pos_point)

  if (is_small_enough(neg_point, pos_point)) :
    return mid_point
  else :
    return test_new_mid_point(function, neg_point, pos_point, mid_point)
	
#tests the function value of the new mid point and checks if the value is
#above or below the tolerance range
def test_new_mid_point(function, neg_point, pos_point, mid_point) :
  function_value = function(mid_point)
  
  if (function_value < tolerance_range) :
    return function_value_less_than_tolerance(function, \
                                              function_value, \
                                              neg_point, \
                                              pos_point, \
                                              mid_point)
  elif (function_value > tolerance_range) : 
    return function_value_greater_than_tolerance(function, \
                                                 function_value, \
                                                 neg_point, \
                                                 pos_point, \
                                                 mid_point)
  else :
    return mid_point

#if the function value is less than the tolerance call the correct interval_search on the correct
#interval
def function_value_less_than_tolerance(function, function_value, neg_point, pos_point, mid_point) :
  if ((function(pos_point) - tolerance_range) < function_value) :
    return interval_search(function, neg_point, mid_point) 
  else :       
    return interval_search(function, mid_point, pos_point)

#if the function value is greater than the tolerance call the correct interval_search on the correct
#interval
def function_value_greater_than_tolerance(function, function_value, neg_point, pos_point, mid_point) :
  if ((function(neg_point) - tolerance_range) > function_value) :
    return interval_search(function, pos_point, mid_point)
  else :
    return interval_search(function, mid_point, neg_point)
  
#these are the functions that will be tested
def poly_01(x) : return (x ** 3) - (2 * x) - 3
def poly_02(x) : return (x ** 5) - (5 * x) - 5
def poly_03(x) : return -x + 2
def poly_04(x) : return math.cos(x)

#finds each mid point where the function given on a certain
#interval equals zero
mid_point_01 = interval_search(poly_01, 1.0, 2.0)
mid_point_02 = interval_search(poly_02, 1.0, 2.0)
mid_point_03 = interval_search(poly_03, 1.0, 10.0)
mid_point_04 = interval_search(poly_04, 9.0, 12.0)

#prints out each midpoint for each function where the function
#equals zero and then it prints it the fuction given that point.
print "mid_point_01: " + str(mid_point_01)
print "poly_01: " + str(round(poly_01(mid_point_01), 8)) + "\n"

print "mid_point_02: " + str(mid_point_02)
print "poly_02: " + str(round(poly_02(mid_point_02), 8)) + "\n"

print "mid_point_03: " + str(mid_point_03)
print "poly_03: " + str(round(poly_03(mid_point_03), 8)) + "\n"

print "mid_point_04: " + str(mid_point_04)
print "poly_04: " + str(round(poly_04(mid_point_04), 8)) + "\n"
