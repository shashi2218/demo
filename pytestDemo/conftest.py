import pytest


@pytest.fixture(scope="class")
def setup():
    print("1st execution")
    yield
    print("last execution")

@pytest.fixture()
def dataLoad():
    print("Hi")
    return ["Shashi","Rampur","hishashi.com"]

@pytest.fixture(params=[("chrome","Shashi"),("firefox","RAmpur"),("IE","SS")])
def crossBrowser(request):
    return request.param
