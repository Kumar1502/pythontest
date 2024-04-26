""" This module will have functions to calculate lumpsum returns

Author: Kumar
Date: 21/Apr/2024
"""

def returns(principal,interest_rate,time_in_years,n=1):
    """
    This function calculates lumpsum returns

    Arguments:
        principal: present value of investment
        interest_rate:
        time_in_years: Duration of investment
        n: Number of compunded interests in year
    
    """
    result=principal * (1 + (interest_rate/100)/n)**(n*time_in_years)
    return round(result,2)

