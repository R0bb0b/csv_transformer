# CSV Transformer

This project is an answer to a coding challenge and is desiged to accept a file path and json configuration, transform the csv data and then output transformed data to the requestor.

### Usage
Help output: python3 parse.py --help
```
usage: parse.py [-h] [--output_header [OUTPUT_HEADER]] [--proc_dist {even,odd,ranged}] [--proc_range_start {0,1,2,3,4,5,6,7,8,9}]
                [--proc_range_end {0,1,2,3,4,5,6,7,8,9}]
                csv config

Data Infrastructure Assessment

positional arguments:
  csv                                       Path to the CSV file
  config                                    Path to the JSON config file

optional arguments:
  -h, --help                                show this help message and exit
  --output_header [OUTPUT_HEADER]           Include the header in the output
  --proc_dist {even,odd,ranged}             Parallel process mode
  --proc_range_start {0,1,2,3,4,5,6,7,8,9}  Ranged mode start, requires --proc_dist=ranged
  --proc_range_end {0,1,2,3,4,5,6,7,8,9}    Ranged mode end, requires --proc_dist=ranged
```

### Example Usage:
process data/data.csv with data/config.json with a process distribution of all numbers ending in 0-2
```
python3 parse.py data/data.csv data/config.json --proc_dist=ranged --proc_range_start=0 --proc_range_end=2
```

process data/data.csv with data/config.json with a process distribution of all even rows
```
python3 parse.py data/data.csv data/config.json --proc_dist=even
```

process data/data.csv with data/config.json with a process distribution of all odd rows
```
python3 parse.py data/data.csv data/config.json --proc_dist=odd
```

process data/data.csv with data/config.json with a single process
```
python3 parse.py data/data.csv data/config.json
```

process data/data.csv with data/config.json with a single process and header
```
python3 parse.py data/data.csv data/config.json --output_header
```

tested configuration:
```
{
    "spec_version":1.0,
    "transforms":[
        {
            "operation":"slugify",
            "column":"RecordLocation"
        },
        {
            "operation":"f-to-c",
            "column":"Temperature"
        },
        {
            "operation":"hst-to-unix",
            "column":"RecordedTime",
            "date_reference":"RecordedDate",
            "time_format":"%H:%M:%S",
            "date_format":"%m/%d/%y"
        },
        {
            "operation":"hst-to-unix",
            "column":"TimeSunRise",
            "date_reference":"RecordedDate",
            "time_format":"%H:%M:%S",
            "date_format":"%m/%d/%y"
        },
        {
            "operation":"hst-to-unix",
            "column":"TimeSunSet",
            "date_reference":"RecordedDate",
            "time_format":"%H:%M:%S",
            "date_format":"%m/%d/%y"
        }
    ]
}
```

Date and time format codes can be found here: https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes

### Prerequisites

Tested Python version: 3.6.9
but should work with any 3.3+ version

Additional Python libraries: pytz, pytest, pytest-cov

Data set used to test with: https://docs.google.com/document/d/1aZN_OALd3dRLwK7iI-K4Qbihm5Oi0_3-GZ0MKaz7PTI/edit

### Installing

Install python 3: If you have questions about how to install Python 3 on your platform you can reference the getting started guide here: https://www.python.org/about/gettingstarted/ 

pip 3 should already be installed with your Python 3 version, but if it is not you can find their documentation here: https://pip.pypa.io/en/stable/installing/

Installing additionaly Python libraries:

`sudo pip3 install pytz`

`sudo pip3 install pytest`

`sudo pip3 install pytest-cov`


## Running the tests

navigate to the testing/unittests directory:
```
cd testing/unittests
```

Run tests
```
python3 -m pytest
```

Run tests with code coverage report
```
python3 -m pytest --cov-report term-missing --cov=../../lib
```

## Author

* **Robert Baldessari** - (https://github.com/R0bb0b)
