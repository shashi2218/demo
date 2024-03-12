import pytest


@pytest.mark.smoke
def test_firstprogram():
    print("Hello Shashi")


@pytest.mark.xfail
def test_secondgreetcreditcard():
    print("Hello Rohit")

def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])
