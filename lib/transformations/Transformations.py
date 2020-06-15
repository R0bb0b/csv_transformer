import string
from datetime import datetime
from pytz import timezone

class Transformations:
    """
    class housing individual transformations

    ...

    Methods
    -------
    replaceWhiteSpace(strInString, strReplace)
    changeCase(strInString, strOperation)
    removePunctuation(strInString)
    convertTempFtoC(intF)
    convertToUtc(strDateTime, strFormat)
    """
    def replaceWhiteSpace(self, strInString: str, strReplace: str) -> str:
        """
		return string with white space replaced with character

        Parameters
        ----------
        strInString : str
            haystack
        strReplace : str
            character with which to replace white space
        """
        return "-".join(strInString.split())

    def changeCase(self, strInString: str, strOperation: str) -> str:
        """
		convert string to upper or lower case

        Parameters
        ----------
        strInString : str
            string to fix
        strOperation : str
            which case to convert to, either upper or lower
        """
        if strOperation == "lower":
            return strInString.lower()
        elif strOperation == "upper":
            return strInString.upper()

    def removePunctuation(self, strInString) -> str:
        """
		remove all punctuation from string

        Parameters
        ----------
        strInString : str
            string to fix
        """
        return strInString.translate(str.maketrans('', '', string.punctuation))

    def convertTempFtoC(self, intF: int) -> int:
        """
		convert Fahrenheit to Celsius

        Parameters
        ----------
        intF : int
            number to convert
        """
        return round((int(intF) - 32) / 1.8, 1)

    def convertToUtc(self, strDateTime: str, strFormat: str) -> object:
        """
		convert timestamp to UTC, Hawaii timezone is assumed

        Parameters
        ----------
        strDateTime : str
            the time stamp to convert
        strFormat : str
            the format of strDateTime
        """
        datetime_obj_hawaii = timezone('US/Hawaii').localize(datetime.strptime(strDateTime, strFormat))
        return datetime_obj_hawaii.astimezone(timezone('UTC'))
