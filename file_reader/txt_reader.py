import traceback
import pandas as pd
from file_reader.file_reader import RequestReader
from file_reader.validate_request import ValidateRequest

class TxtReader(RequestReader):

    def read_file(self, filename):
        try:
            data = pd.read_csv(filename, sep=' ', header=None)
            request = [list(i) for i in data.values]
            return ValidateRequest().validate(request)
        except FileNotFoundError:
            print('Invalid file name; please provide valid file path as first argument. E.g. python main.py test.txt')
        except pd.errors.EmptyDataError:
            print("File is empty")
        except:
            print("Error occured while retriving the file")
            print(traceback.print_stack())
        return False






