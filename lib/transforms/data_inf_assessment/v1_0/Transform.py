class Transform:
    """
    class housing transformations, depending on Transformations object

    ...

    Methods
    -------
    slugify(strInStr)
    fToC(strInStr)
    hstToUnix(strInStr)
    """
    def __init__(self, objTransformations):
        """
        Parameters
        ----------
        objTransformations : object
            object containing individual transformation logic
        """
        self.objTransformations = objTransformations

    def slugify(self, strInStr: str) -> str:
        """
		return a slugified string

        Parameters
        ----------
        strInStr : str
            the string to be modified
        """
        strInStr = self.objTransformations.removePunctuation(strInStr)
        strInStr = self.objTransformations.replaceWhiteSpace(strInStr, "-")
        strInStr = self.objTransformations.changeCase(strInStr, "lower")

        return strInStr
        
    def fToC(self, intF: int) -> float:
        """
		convert Fahrenheit to Celsius

        Parameters
        ----------
        intF : int
            Fahrenheit
        """
        intC = self.objTransformations.convertTempFtoC(intF)

        return intC

    def hstToUnix(self, strTimeStamp: str, strDateTimeFormat: str) -> int:
        """
		convert a timestamp to UTC and return linux timestamp

        Parameters
        ----------
        strTimeStamp : str
            timestamp to convert
        strDateTimeFormat : str
            the format with which to use to parse strTimeStamp
        """
        objDateTime = self.objTransformations.convertToUtc(strTimeStamp, strDateTimeFormat)
        return round(objDateTime.timestamp())
