import sys, os, pytest

from datetime import datetime
from unittest.mock import Mock

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../../../../lib"))

from transforms.data_inf_assessment.v1_0.Transform import Transform

def test_Slugify():
    objMock_Transformations = Mock()
    objMock_Transformations.removePunctuation = Mock(return_value="test")
    objMock_Transformations.replaceWhiteSpace = Mock(return_value="test")
    objMock_Transformations.changeCase = Mock(return_value="test")

    objTransform = Transform(objMock_Transformations)
    assert objTransform.slugify("test") == "test"

def test_fToC():
    objMock_Transformations = Mock()
    objMock_Transformations.convertTempFtoC = Mock(return_value=2)

    objTransform = Transform(objMock_Transformations)
    assert objTransform.fToC(1) == 2

def test_hstToUnix():
    objMock_Transformations = Mock()
    objMock_Transformations.convertToUtc = Mock(return_value=datetime.now())

    objTransform = Transform(objMock_Transformations)
    assert str(objTransform.hstToUnix("test", "test")).isnumeric();
