import pytest
#---------------------------------------
# fun to handle pass case
#---------------------------------------
def test_fun():
    assert 1+1==2
#---------------------------------------
# fun to handle fail case
#---------------------------------------
def test_fun_fail():
    a=1
    b=2
    c=3
    assert a+b ==c
#---------------------------------------
# fun to handle exception
#---------------------------------------
def test_divide_fun():
    with pytest.raises(ZeroDivisionError) as e:
      num = 1 / 0

    assert 'division by zero' in str(e.value)
    