""" 
This module will have functions to calculate monthly investement returns

Author: Kumar
Date: 21/Apr/2024


Assumptions:

FV = P × ({[1 + i]^n – 1} / i) × (1 + i).

In the above formula –

FV is the amount you receive upon maturity.
P is the amount you invest at regular intervals.
n is the number of payments you have made.
i is the SIP periodic rate of interest.
"""

def returns(invested_amount,return_rate,total_period_in_years):
    """
    This function calculates sip returns

    Arguments:
        principal: present value of investment
        interest_rate:
        time_in_years: Duration of investment
        n: Number of compunded interests in year
    
    """
    n=total_period_in_years*12
    if return_rate==0:
        return invested_amount*n
    i=(return_rate/12)/100
    future_value= invested_amount * (((1+i)**(n)-1)/i)*(1+i)
    return round(future_value,2)

