import sys, os, argparse, json, pprint, csv

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), "lib"))

from transforms.data_inf_assessment.GetInfAssessmentTransform import GetInfAssessmentTransform
from transformations.Transformations import Transformations
from file_proc.FileIterator import FileIterator

objParser = argparse.ArgumentParser(
    prog='parse.py',
    formatter_class=lambda prog: argparse.HelpFormatter(prog,max_help_position=50,width=160), 
    description='Data Infrastructure Assessment'
)

objParser.add_argument('csv', type=str, help="Path to the CSV file")
objParser.add_argument('config', type=str, help="Path to the JSON config file")
objParser.add_argument('--output_header', nargs='?', const=True, default=False, help="Include the header in the output")
objParser.add_argument('--proc_dist', type=str, choices=['even', 'odd', 'ranged'], help="Parallel process mode")
objParser.add_argument('--proc_range_start', type=int, choices=range(0, 10), help="Ranged mode start, requires --proc_dist=ranged")
objParser.add_argument('--proc_range_end', type=int, choices=range(0, 10), help="Ranged mode end, requires --proc_dist=ranged")

dicArgs = objParser.parse_args()

#convert json configuration to dictionary
dicConfig = {}
with open(dicArgs.config) as fp:
    dicConfig = json.load(fp)

#convert the operation to a syntactically correct method string
for intKey, dicTransform in enumerate(dicConfig["transforms"]):
    listOperation = dicTransform["operation"].split("-")
    strOperation = "".join(
        list(
            map(
                lambda x:x.capitalize(),
                listOperation
            )
        )
    )

    dicConfig["transforms"][intKey]["operation"] = strOperation[0].lower() + strOperation[1:]

#set the version of the transform logic
strVersion = str(dicConfig["spec_version"])

#get the transform object from the transformation factory
objTransformations = Transformations()
objTransform = GetInfAssessmentTransform().getObject(strVersion, objTransformations)

objCsvWriter = csv.writer(sys.stdout)

intCounter = 0
lstHeader = None

#instantiate the file iterator
objFileIterator = FileIterator(dicArgs.csv, dicArgs.proc_dist, dicArgs.proc_range_start, dicArgs.proc_range_end)

#loop through the qualified lines of the file
for dicLine in objFileIterator.iterate():
    intCounter += 1

    #if we are to output the header then output it
    if dicArgs.output_header is True and intCounter == 1:
        objCsvWriter.writerow(objFileIterator.getHeader())

    #loop through and apply the transformations from the configuration
    for dicTransform in dicConfig["transforms"]:
        if hasattr(objTransform, dicTransform["operation"]):
            #if date is separate from time in the csv data then set the date reference
            if "date_reference" in dicTransform:
                dicLine[dicTransform["column"]] = dicLine[dicTransform["date_reference"]] + " " + dicLine[dicTransform["column"]]

            #if time format and date format have been defined in the config then assume we are working with a date/time
            if "time_format" in dicTransform and "date_format" in dicTransform:
                dicLine[dicTransform["column"]] = getattr(objTransform, dicTransform["operation"])(dicLine[dicTransform["column"]], dicTransform["date_format"] + " " + dicTransform["time_format"])
            else:
                dicLine[dicTransform["column"]] = getattr(objTransform, dicTransform["operation"])(dicLine[dicTransform["column"]])
        else:
            #the requested operation doesn't exist, so error out and end processing
            raise ValueError("operation " + dicTransform["operation"] + " doesn't exist")
    
    objCsvWriter.writerow(dicLine.values())
