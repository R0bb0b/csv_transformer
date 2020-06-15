import sys, os, pytest

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../../../../lib"))

from transforms.data_inf_assessment.GetInfAssessmentTransform import GetInfAssessmentTransform

def test_missing_version():
    with pytest.raises(ImportError):
        objTransform = GetInfAssessmentTransform().getObject("2.0", False)

def test_get_transform():
    objTransform = GetInfAssessmentTransform().getObject("1.0", False)

    assert type(objTransform).__name__ == "Transform"
