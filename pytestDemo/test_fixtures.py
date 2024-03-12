import pytest



@pytest.mark.usefixtures("setup")

class TestExample:

    def test_fixtures(self):
        print("all 1test cases will be executed here")

    def test_fixtures2(self):
        print("all 2test cases will be executed here")

    def test_fixtures3(self):
        print("all 3test cases will be executed here")

    def test_fixtures4(self):
        print("all 4test cases will be executed here")

    def test_fixtures5(self):
        print("all 5test cases will be executed here")

