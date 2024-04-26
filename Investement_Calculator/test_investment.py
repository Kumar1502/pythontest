"""This modlue will have tests
"""


from calculators.lumpsum import returns as lumpsum_returns
from calculators.sip import returns as sip_returns

def test_lumpsum():
    assert(lumpsum_returns(1000, 0, 15))==1000
    
def test_sip():
    assert(sip_returns(1000, 0, 2))==24000