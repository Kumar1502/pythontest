from workshop.calculator import add

def test_add():
    """
    This function test add functionality
    """
    assert add(1,2)==3
    assert add(9,9)==18
    assert add(0,0)==0
    assert add(9,6)==15