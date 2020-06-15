import sys, os, pytest

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../../../../lib"))

from transformations.Transformations import Transformations

def test_replaceWhiteSpace():
    objTransformations = Transformations()

    assert objTransformations.replaceWhiteSpace("test test", "-") == "test-test"

def test_changeCaseLower():
    objTransformations = Transformations()

    assert objTransformations.changeCase("TeStInG", "lower") == "testing"

def test_changeCaseUpper():
    objTransformations = Transformations()

    assert objTransformations.changeCase("TeStInG", "upper") == "TESTING"

def test_removePunctuation():
    objTransformations = Transformations()

    assert objTransformations.removePunctuation("t.e-s!t") == "test"

def test_convertTempFtoC():
    objTransformations = Transformations()

    assert objTransformations.convertTempFtoC(100) == 37.8

def test_convertToUtc():
    objTransformations = Transformations()

    assert str(objTransformations.convertToUtc("9/29/16 23:55:26", "%m/%d/%y %H:%M:%S")) == "2016-09-30 09:55:26+00:00"
