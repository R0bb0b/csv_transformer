import sys, os, pytest

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../../../../lib"))

from file_proc.FileIterator import FileIterator

def test_ranged_missing_start():
    with pytest.raises(ValueError):
        objFileIterator = FileIterator("data.csv", "ranged", None, 2)

def test_ranged_missing_end():
    with pytest.raises(ValueError):
        objFileIterator = FileIterator("data.csv", "ranged", 1)

def test_ranged():
    objFileIterator = FileIterator("data.csv", "ranged", 1, 2)

    for dicLine in objFileIterator.iterate():
        assert dicLine["rownum"] in ["1", "2"]

def test_even():
    objFileIterator = FileIterator("data.csv", "even")

    for dicLine in objFileIterator.iterate():
        assert dicLine["rownum"] in ["2", "4"]

def test_odd():
    objFileIterator = FileIterator("data.csv", "odd")

    for dicLine in objFileIterator.iterate():
        assert dicLine["rownum"] in ["1", "3"]

def test_all():
    objFileIterator = FileIterator("data.csv")

    intCounter = 0
    for dicLine in objFileIterator.iterate():
        intCounter += 1
        assert dicLine["rownum"] in ["1", "2", "3", "4"]

    assert intCounter == 4

def test_header():
    objFileIterator = FileIterator("data.csv")

    lstHeader = []
    for dicLine in objFileIterator.iterate():
        lstHeader = objFileIterator.getHeader()
        break

    assert len(lstHeader) == 5

def test_invalid_proc_distribution():
    objFileIterator = FileIterator("data.csv", "none")

    for dicLine in objFileIterator.iterate():
        assert dicLine == False
