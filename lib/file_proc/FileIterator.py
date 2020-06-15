import csv

class FileIterator:
    """
    Class for file line iteration

    ...

    Attributes
    ----------
    strFileName : str
        the name and path of the file to iterate
    strProcDistMode : str
        the process distribution mode
    intRangedStart : int
        range start for ranged distribution mode
    intRangedEnd : int
        range end for ranged distribution mode
    lstHeader : list
        the file header

    Methods
    -------
    iterate()
	getHeader()
    yieldLine()
    """

    strFileName = None
    strProcDistMode = None
    intRangedStart = None
    intRangedEnd = None
    lstHeader = None

    def __init__(self, strFileName: str, strProcDistMode: str = None, intRangedStart: int = None, intRangedEnd: int = None):
        """
        Parameters
        ----------
        strFileName : str
            the name and path of the file to iterate

        strProcDistmode : str
            the process distribution mode, options are None, odd, even and ranged

        intRangedStart : int
            ranged start for ranged distribution mode

        intRangedEnd : int
            ranged end for ranged distribution mode
        """
        self.strFileName = strFileName
        self.strProcDistMode = strProcDistMode
        self.intRangedStart = intRangedStart
        self.intRangedEnd = intRangedEnd

        if self.strProcDistMode == "ranged" and (self.intRangedStart is None or self.intRangedEnd is None):
            raise ValueError("proc_range_start and proc_range_end are required for ranged process distribution")

    def iterate(self) -> dict:
        """
		generator to yield the next line in the file in accordance to the process distribution mode
        """ 
        with open(self.strFileName) as fp:
            reader = csv.DictReader(fp, delimiter=',', quotechar='"')

            intCounter = 0
            for line in reader:
                intCounter += 1

                if intCounter == 1:
                    self.lstHeader = list(line.keys())
                    
                if self.yieldLine(intCounter):
                    yield line

    def getHeader(self) -> list:
        """
		return the file header as a list
        """
        return self.lstHeader

    def yieldLine(self, intCounter: int) -> bool:
        """
		determine if the current line in the file qualifies for a yeild by the generator

        Parameters
        ----------
        intCounter : int
            the current line in of the file
        """
        if self.strProcDistMode is None:
            return True
        elif self.strProcDistMode == "even":
            if intCounter % 2 == 0:
                return True
        elif self.strProcDistMode == "odd":
            if intCounter % 2 == 1:
                return True
        elif self.strProcDistMode == "ranged":
            intProcCount = intCounter // 10**0 % 10
            if intProcCount >= self.intRangedStart and intProcCount <= self.intRangedEnd:
                return True
        else:
            return False

        return False
