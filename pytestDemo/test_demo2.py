import pytest

@pytest.mark.skip
def test_firstprogram(setup):
    messsage = "Hello"
    assert  messsage == "hi", "Test failed bec  string do not match"

@pytest.mark.smoke
def test_secondcreditcard():
    a = 4
    b = 6
    assert a+2 == 6, "Addition do not match"
