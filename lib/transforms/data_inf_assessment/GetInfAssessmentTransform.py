from importlib import import_module

class GetInfAssessmentTransform:
    """
    Factory to return the requested version of Transform

    ...

    Methods
    -------
    getObject(strVersion, objTransformations)
    """
    def getObject(self, strVersion: str, objTransformations) -> object:
        """
		return the requested version of transform

        Parameters
        ----------
        strVersion : str
            the version of Transform to be returned
        objTransformations : object
            the object containing individual transformation logic

        Raises
        ----------
        ImportError
            if the requested version cannot be found
        """
        try:
            objInfAssessment = import_module("transforms.data_inf_assessment.v" + strVersion.replace(".", "_") + ".Transform")
        except:
            raise ImportError(strVersion + " is not a valid version of Transform")

        strClass = getattr(objInfAssessment, "Transform")
        return strClass(objTransformations)
