from file_reader.file_reader import RequestReader
import pandas as pd

class TxtReader(RequestReader):

    def read_file(self, filename):
        try:
            data = pd.read_csv(filename, sep=' ', header=None)
            request = [list(i) for i in data.values]
            # request =
            # for index, row in data.iterrows():
            #     request[0].append(row[0])
            #     request[1].append(row[1]+0)
            return request
        except FileNotFoundError:
            print('Invalid file name; please provide valid file path as first argument. E.g. python main.py test.txt')
        except:
            print('Invalid data in file, please provide a valid file')
        return False


