import os
from file_handler.file_writer import FileWriter

class TxtWriter(FileWriter):

    def write_file(self, allocations):
        cwd = os.getcwd()
        output = []
        for i in allocations:
            temp = ''
            for j in i:
                if len(temp) == 0: temp += j + ' '
                else: temp += j + ','
            output.append(temp[:-1])
        with open(cwd + '\output\Walmart.txt', 'w') as filehandle:
            filehandle.writelines("%s\n" % place for place in output)
        return "\nOutput file is located at: "+ cwd + '\output\Walmart.txt'