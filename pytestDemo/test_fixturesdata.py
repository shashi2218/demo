import pytest

from pytestDemo.Baseclass import baseclass


@pytest.mark.usefixtures("dataLoad")

class Testexample2(baseclass):
    def test_editprofile(self,dataLoad):
        log =self.getlogger()
        log.info(dataLoad[1])
        log.info(dataLoad[2])

